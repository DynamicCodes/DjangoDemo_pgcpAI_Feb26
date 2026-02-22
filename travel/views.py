from django.shortcuts import render

from travel.models import Destination


# Create your views here.
def index(request):
    ''' for manual send data to index
    des1 = Destination()
    des1.name = "mumbai"
    des1.days = 19
    des1.offer = True
    '''

    # send by DB
    des1 = Destination.objects.all()

    return render(request, 'index.html', {'des1':des1})