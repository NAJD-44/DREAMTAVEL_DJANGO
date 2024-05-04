from django.shortcuts import render, redirect
from .models  import Promotion
# Create your views here.
def promotion(request):
    return render(request,"promotions/promotion.html")

def promotions(request):
    return render(request,"promotions/promotions.html")    

def createPromotion(request):
    return render(request,"promotions/createPromotion.html")

def insertPromotion(request):
   titre = request.POST['titre']
   description = request.POST['description']
   validite = request.POST['validite']
   ps=Promotion(titre=titre,description=description,validite=validite)
   ps.save()
   return redirect('readPromotion')
   return render(request,"promotions/promotion.html") 

def readPromotion(request):
    att = Promotion.objects.all()
    return render(request,"promotions/readProm.html",{"Promotiondata":att})

def deletePromotion(request, id):
    d =Promotion.objects.get(id=id)
    d.delete()
    return redirect("../../readProm")


def edit(request, id):
    a =Promotion.objects.get(id=id)
    return render(request,"promotions/editProm.html",{'Promotiondata':a})

def updatePromotion(request, id):
    a = Promotion.objects.get(id=id)
    titre = request.POST['titre']
    description = request.POST['description']
    validite = request.POST['validite']
    a.titre = titre
    a.description = description
    a.validite= validite
    a.save()
    return redirect("../../readProm")   

