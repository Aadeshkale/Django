from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    x="<h1> Working Fine : ) </h1>"
    return HttpResponse(x)

def contact(request):
    c='''<h2>
        Name:Aadesh S. Kale<br>
        Mobile:842168...5<br>
        Email:aadeshk.....@gamil.com<br>
        </h2>
    '''
    return HttpResponse(c)
def books(request):
    y='''
        <h1>Book1</h1>
        <h1>Book2</h1>
        <h1>Book3</h1>
    '''
    return HttpResponse(y)