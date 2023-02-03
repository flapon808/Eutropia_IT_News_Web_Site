from django.shortcuts import render
from Newsfeed.models import Employees
# Create your views here.
def home (request):
    emp = Employees.object.all()
    context = {
        'emp': emp
    }
    return render(request, 'index.html')