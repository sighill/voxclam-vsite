from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse , HttpResponseRedirect

def mapClemence(request):
	template = loader.get_template('mapClemence.html')
	context = {}
	return HttpResponse(template.render(context, request))