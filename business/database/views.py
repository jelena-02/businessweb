from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import People, Timing
from .forms import PeopleCheck
from django.core.exceptions import ObjectDoesNotExist

def index(request):
	
	return render(request, 'database/base.html')

def doesnotexist(request):
	return render(request, 'database/nope.html')


def answer(request):
	if request.method == 'POST':
		person = PeopleCheck(request.POST)
		if person.is_valid():
			fullname = person.cleaned_data['currentperson'].split (' ')
			try:
				persondata = People.objects.get(name__iexact = str(fullname[0]), lastname__iexact = str(fullname[1]))
			except ObjectDoesNotExist:
				return HttpResponseRedirect(reverse('dne'))
			instances = Timing.objects.filter(number = persondata.number)
			personal = persondata.name + ' ' + persondata.lastname
			context = {'persona': personal, 'answers': instances}
			return render(request, 'database/results.html', context)
			
			
			
	else:
		person = PeopleCheck()
	
	return render(request, 'database/tally.html', {'form': person})
		
		
	
# Create your views here.
