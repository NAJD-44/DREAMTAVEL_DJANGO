from django.shortcuts import render, redirect
from .models  import Attraction
# Create your views here.
def attraction(request):
    return render(request,"attractions/attraction.html")

def attractions(request):
    return render(request,"attractions/attractions.html")    

def createAttraction(request):
    return render(request,"attractions/createAttraction.html")

def insertAttraction(request):
   name = request.POST['name']
   description = request.POST['description']
   image = request.FILES.get('image')
   a=Attraction(name=name,description=description,image=image)
   a.save()
   return redirect('readAtt') 
   return render(request,"attractions/readAtt.html") 

def readAtt(request):
    att = Attraction.objects.all()
    return render(request,"attractions/readAtt.html",{"Attractiondata":att})

def deleteAttraction(request, id):
    a =Attraction.objects.get(id=id)
    a.delete()
    return redirect("../../readAtt")


def edit(request, id):
    a =Attraction.objects.get(id=id)
    return render(request,"attractions/editAttraction.html",{'Attractiondata':a})

def updateAttraction(request, id):
    a = Attraction.objects.get(id=id)
    name = request.POST['name']
    description =  request.POST['description']
    image = request.FILES.get('image')
    a.name = name
    a.description = description
    a.image= image
    a.save()
    return redirect("../../readAtt")
