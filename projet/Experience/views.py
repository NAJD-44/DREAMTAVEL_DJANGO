from django.shortcuts import render
from .models  import Experience
# Create your views here.
def experience(request):
    return render(request,"experiences/experience.html")

def experiences(request):
    return render(request,"experiences/experiences.html")    

def createExperience(request):
    return render(request,"experiences/createExperience.html")

def insertExperience(request):
   rate = request.POST['rate']
   comment = request.POST['comment']
   es=Experience(rate=rate,comment=comment)
   es.save()
   return render(request,"experiences/experience.html") 
def readExperience(request):
    att = Experience.objects.all()
    return render(request,"experiences/readExp.html",{"Experiencedata":att})

def deleteExperience(request, id):
    d =Experience.objects.get(id=id)
    d.delete()
    return redirect("../../readExp")


def edit(request, id):
    a =Experience.objects.get(id=id)
    return render(request,"experiences/editExp.html",{'Experiencedata':a})

def updateExperience(request, id):
    a = Experience.objects.get(id=id)
    rate = request.POST['rate']
    comment = request.POST['comment']
    a. rate =   rate
    a.comment =  comment
    a.save()
    return redirect("../../readExp")   
