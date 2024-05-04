from django.shortcuts import render, redirect
from .models  import Transport
# Create your views here.
def transport(request):
    return render(request,"transports/transport.html")

def transports(request):
    return render(request,"transports/transports.html")    

def createTransport(request):
    return render(request,"transports/createTransport.html")

def insertTransport(request):
   name = request.POST['name']
   type_transport = request.POST['typet']
   description = request.POST['description']
   image = request.FILES.get('image')
   ts=Transport(name=name,type_transport=type_transport,description=description,image=image)
   ts.save()
   return redirect('readTransport')
   return render(request,"transports/transport.html") 

def readTransport(request):
    att = Transport.objects.all()
    return render(request,"transports/readTra.html",{"Transportdata":att})

def deleteTransport(request, id):
    d =Transport.objects.get(id=id)
    d.delete()
    return redirect("../../readTra")


def edit(request, id):
    a =Transport.objects.get(id=id)
    return render(request,"transports/editTra.html",{'Transportdata':a})

def updateTransport(request, id):
    a = Transport.objects.get(id=id)
    name = request.POST['name']
    type_transport = request.POST['typet']
    description = request.POST['description']
    image = request.FILES.get('image')
    a.name = name
    a.type_transport = type_transport
    a.description = description
    a.image = image
    a.save()
    return redirect("../../readTra")   
