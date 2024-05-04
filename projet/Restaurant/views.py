from django.shortcuts import render, redirect
from .models  import Restaurant
# Create your views here.
def restaurant(request):
    return render(request,"restaurants/restaurant.html")

def restaurants(request):
    return render(request,"restaurants/restaurants.html")    

def createRestaurant(request):
    return render(request,"restaurants/createRestaurant.html")

def insertRestaurant(request):
   name = request.POST['name']
   type_cuisine = request.POST['typec']
   description = request.POST['description']
   image = request.FILES.get('image')
   rs=Restaurant(name=name,type_cuisine=type_cuisine ,description=description,image=image)
   rs.save()
   return redirect('readRestaurant')
   return render(request,"restaurants/restaurant.html") 
def readRestaurant(request):
    att = Restaurant.objects.all()
    return render(request,"restaurants/readRes.html",{"Restaurantdata":att})

def deleteRestaurant(request, id):
    d =Restaurant.objects.get(id=id)
    d.delete()
    return redirect("../../readRes")


def edit(request, id):
    a =Restaurant.objects.get(id=id)
    return render(request,"restaurants/editRes.html",{'Restaurantdata':a})

def updateRestaurant(request, id):
    a = Restaurant.objects.get(id=id)
    name = request.POST['name']
    type_cuisine = request.POST['typec']
    description = request.POST['description']
    image = request.FILES.get('image')
    a.name =  name
    a.type_cuisine =  type_cuisine
    a.description =  description
    a.image= image
    a.save()
    return redirect("../../readRes")   
