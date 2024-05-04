from django.shortcuts import render, redirect
from .models  import Reservation
# Create your views here.
def reservation(request):
    return render(request,"reservations/reservation.html")

def reservations(request):
    return render(request,"reservations/reservations.html")    

def createReservation(request):
    return render(request,"reservations/createReservation.html")

def insertReservation(request):
   date_reservation=request.POST['dateres']
   rs=Reservation(date_reservation=date_reservation)
   rs.save()
   return redirect('readReservation')
   return render(request,"reservations/reservation.html") 
def readReservation(request):
    att = Reservation.objects.all()
    return render(request,"reservations/readRes.html",{"Reservationdata":att})

def deleteReservation(request, id):
    d =Reservation.objects.get(id=id)
    d.delete()
    return redirect("../../readRes")


def edit(request, id):
    a =Reservation.objects.get(id=id)
    return render(request,"reservations/editRes.html",{'Reservationdata':a})

def updateReservation(request, id):
    a = Reservation.objects.get(id=id)
    date_reservation=request.POST['dateres']
    a.date_reservation = date_reservation
    a.save()
    return redirect("../../readRes")   
