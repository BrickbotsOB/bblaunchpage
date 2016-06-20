from django.conf import settings
from django.shortcuts import render

def privacy(request):
	context = {
	"title":"Privacy Policy",
	}

	template = "privacy.html"
	return render(request, template, context)