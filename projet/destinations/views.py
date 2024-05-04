from django.shortcuts import render, redirect
from .models  import Destination
# Create your views here.
def destination(request):
    return render(request,"destinations/destination.html")

def destinations(request):
    return render(request,"destinations/destinations.html")    

def createDestination(request):
    return render(request,"destinations/createDestination.html")

def insertDestination(request):
   name = request.POST['name']
   content = request.POST['content']
   image = request.FILES.get('image')
   ds=Destination(name=name,content=content,image=image)
   ds.save()
   return redirect('readDestination') 
   return render(request,"destinations/readDestination.html") 

def readDestination(request):
    att = Destination.objects.all()
    return render(request,"destinations/readDes.html",{"Destinationdata":att})

def deleteDestination(request, id):
    d =Destination.objects.get(id=id)
    d.delete()
    return redirect("../../readDes")


def edit(request, id):
    a =Destination.objects.get(id=id)
    return render(request,"destinations/editDestination.html",{'Destinationdata':a})

def updateDestination(request, id):
    a = Destination.objects.get(id=id)
    name = request.POST['name']
    content = request.POST['content']
    image = request.FILES.get('image')
    a.name = name
    a.content = content
    a.image= image
    a.save()
    return redirect("../../readDes")   
