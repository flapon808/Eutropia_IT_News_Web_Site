from django.shortcuts import render,redirect
from example.form import registrationform
from example.models import registration
# Create your views here.

def emp(request):
    if request.method == 'POST':
        form = registrationform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except: 
                pass
        
    else: 
        form  = registrationform()
    return render(request, 'index.html', {'form':form})


def show(request):
    employee = registration.objects.all()
    return render(request, 'show.html', {'employee':employee})

def edit(request, id):
    employee = registration.objects.get(id =id)
    return render(request, 'edit.html', {'employee': employee})

def update (request, id):
    employee = registration.objects.get(id =id)
    form = registrationform(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect ("/show")
    
    return render(request, 'edit.html', {'employee': employee})

def delete(request, id):
    employee = registration.objects.get(id = id)
    employee.delete()
    return redirect("/show")