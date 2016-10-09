from about import getCompanyList
from details.models import details
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from pprint import pprint

def homeView(request):
    context = {}
    theList = getCompanyList()
    theDetails = details.objects.filter(company_name__in=theList)

    #theDetails = details.objects.all()
    print(theDetails)
    context['recruiters'] = theDetails
    context['thebomb'] = "Hello!!!"

    return render(request, 'home/home.html', context=context)
