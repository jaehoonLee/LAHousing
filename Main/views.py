from django.shortcuts import render, render_to_response
from django.template import RequestContext
# Create your views here.
def main(request):
    return render_to_response('index.html', RequestContext(request))