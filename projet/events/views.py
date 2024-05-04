from django.shortcuts import render, redirect
from .models  import Event
# Create your views here.
def event(request):
    return render(request,"events/event.html")

def events(request):
    return render(request,"events/events.html",{'event':Event.objects.all()})    

def createEvent(request):
    return render(request,"events/createEvent.html")

def insertEvent(request):
   title = request.POST['title']
   description = request.POST['description']
   location = request.POST['location']
   image = request.FILES.get('image')
   price = request.POST['price']
   es=Event(title=title,description=description,location=location,image=image,price=price)
   es.save()
   return redirect('readEvent') 
   return render(request,"events/readEve.html")

def readEvent(request):
    att = Event.objects.all()
    return render(request,"events/readEve.html",{"Eventdata":att})

def deleteEvent(request, id):
    d =Event.objects.get(id=id)
    d.delete()
    return redirect("../../readEve")


def edit(request, id):
    a =Event.objects.get(id=id)
    return render(request,"events/editEvent.html",{'Eventdata':a})

def updateEvent(request, id):
    a = Event.objects.get(id=id)
    title = request.POST['title']
    description = request.POST['description']
    location = request.POST['location']
    image = request.FILES.get('image')
    price = request.POST['price']
    a.title =  title
    a.description =  description
    a.location =  location
    a.image= image
    a.price= price
    a.save()
    return redirect("../../readEve")   

