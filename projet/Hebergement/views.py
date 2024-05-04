from django.shortcuts import render, redirect
from .models  import Hebergement
# Create your views here.
def hebergement(request):
    return render(request,"hebergements/hebergement.html")

def hebergements(request):
    return render(request,"hebergements/hebergements.html")    

def createHebergement(request):
    return render(request,"hebergements/createHebergement.html")

def insertHebergement(request):
    name = request.POST['name']
    type_hebergement = request.POST['typeh']
    image = request.FILES.get('image')
    description = request.POST['description']
    hs=Hebergement(name=name,type_hebergement=type_hebergement,image=image,description=description)
    hs.save()
    return redirect('readHebergement')
    return render(request,"hebergements/readHeb.html") 


def readHebergement(request):
    att = Hebergement.objects.all()
    return render(request,"hebergements/readHeb.html",{"Hebergementdata":att})

def deleteHebergement(request, id):
    d =Hebergement.objects.get(id=id)
    d.delete()
    return redirect("../../readHeb")


def edit(request, id):
    a =Hebergement.objects.get(id=id)
    return render(request,"hebergements/editHeb.html",{'Hebergementdata':a})

def updateHebergement(request, id):
    a = Hebergement.objects.get(id=id)
    name = request.POST['name']
    type_hebergement = request.POST['typeh']
    image = request.FILES.get('image')
    description = request.POST['description']
    a.name =  name
    a.type_hebergement =  type_hebergement
    a.image= image
    a.save()
    return redirect("../../readHeb")   
