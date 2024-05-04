from django.shortcuts import render, redirect
from .models  import Touriste
# Create your views here.
def touriste(request):
    return render(request,"touristes/touriste.html")

def touristes(request):
    return render(request,"touristes/touristes.html")    

def signup(request):
    return render(request,"touristes/signup.html")    
    

def insertTouriste(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    password = request.POST['password']
    ts=Touriste(firstname=fname,lastname=lname,email=email,password=password)
    ts.save()
    return render(request,"pages/index.html")

def readTouriste(request):
    att = Touriste.objects.all()
    return render(request,"touristes/readTou.html",{"Touristedata":att})

def deleteTouriste(request, id):
    d =Touriste.objects.get(id=id)
    d.delete()
    return redirect("../../readTou")


def edit(request, id):
    a =Touriste.objects.get(id=id)
    return render(request,"touristes/editTou.html",{'Touristedata':a})

def updateTouriste(request, id):
    a = Touriste.objects.get(id=id)
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    password = request.POST['password']
    a.firstname= fname
    a.lastname = lname
    a.email = email
    a.password = password
    a.save()
    return redirect("../../readTou")   

