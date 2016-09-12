"""LPTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main.views import home, site
from sites.models import GA, UK, APAC, ALPHA
import sys
import os

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home)
]


def append_to_urlpatterns(farm):
    urlpatterns.append(url(r'^{0}/{1}$'.format(farm, site_id.id), site, {'account': site_id.id, 'farm': str.upper(farm),
                                                                         'is_legacy': site_id.legacy}))


def generate_tags(farm, site_object):
    """
    From all site objects in the DB, generate a js file containing site_object.site_tag string.

    :param farm: Reflects to the subfolder under static/tags/{farm} in which the js file is created
    :param site_object: The object of Site model, which contains id, tag etc.
    """
    tags_path = '{0}/static/tags/{1}'.format(sys.path[0], str.lower(farm))
    tag = open('{0}/{1}.js'.format(tags_path, site_object.id), 'w')
    tag.write(site_object.site_tag)
    tag.close()
    tag_path = '{0}/{1}.js'.format(tags_path, site_object.id)
    os.chmod(tag_path, 0777)
    print 'Creating file: ', tag_path


def purge_tags():
    """
    Purge all tags from the static folders, they will be re-created from the db on the next loop..
    """
    for farm in ['ga', 'uk', 'apac', 'alpha']:
        tags_path = '{0}/static/tags/{1}'.format(sys.path[0], farm)
        if not os.path.exists(tags_path):
            os.makedirs(tags_path)

        for f in os.listdir(tags_path):
            file_path = os.path.join(tags_path, f)
            os.unlink(file_path)
            print 'Deleting file: ', file_path

purge_tags()


# Iterate over all tables (by farm), get siteids for URL generation and tags for js file generation

for site_id in GA.objects.all():
    append_to_urlpatterns('GA')
    generate_tags('ga', site_id)

for site_id in UK.objects.all():
    append_to_urlpatterns('UK')
    generate_tags('uk', site_id)

for site_id in APAC.objects.all():
    append_to_urlpatterns('APAC')
    generate_tags('apac', site_id)

for site_id in ALPHA.objects.all():
    append_to_urlpatterns('ALPHA')
    generate_tags('alpha', site_id)
