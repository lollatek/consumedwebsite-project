from django.shortcuts import render

from .models import Support, Supportimage


# Create your views here.

def support(request):
	supports = Support.objects.order_by('-catal_number')
	screenshots = Supportimage.objects.order_by('-catal_number')
	return render(request, 'support/support.html',{'support':supports, 'supportimage':screenshots,})
