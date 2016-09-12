from django.shortcuts import render
from sites.models import GA, UK, APAC, ALPHA
from time import strftime


def home(request):
    return render(request, "main/home.html", {'date': strftime("%A, %B %d %Y"),
                                              'farms': {'GA': GA.objects.all(),
                                                        'UK': UK.objects.all(),
                                                        'APAC': APAC.objects.all(),
                                                        'ALPHA': ALPHA.objects.all()}})


def site(request, account, farm, is_legacy):
    if is_legacy:
        version = 'Legacy'
    else:
        version = 'LiveEngage2'
    return render(request, "sites/site.html", {'date': strftime("%A, %B %d %Y"),
                                               'site': account,
                                               'title': '{0} {1} Test Site'.format(farm, version),
                                               'farm': farm,
                                               'farms': {'GA': GA.objects.all(),
                                                         'UK': UK.objects.all(),
                                                         'APAC': APAC.objects.all(),
                                                         'ALPHA': ALPHA.objects.all()}})
