from django.shortcuts import render
from .models import Api1 # E' LA CLASSE CHE CONTIENE I DATI

# Create your views here.
def api(request):
    
    api1 = Api1.objects.all()  # vengono presi tutti i dati del database
    return render(request, 'api/pagina.html', {'api1': api1}) #dict CONTEST
 # i dati del databae vengono passati alla pagina