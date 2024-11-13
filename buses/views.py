from django.shortcuts import render
from .models import Buses, Passenger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    safari = Buses.objects.all()
    return render(request, "buses/index.html", {
        "safaris": safari
    })

@login_required
def info(request, pk):
    safari = Buses.objects.get(pk=pk)
    return render(request, "buses/safariinfo.html", {
        "safari":safari
    })


@login_required
def book(request, pk):
    # Fetch the bus object or return a 404 error if not found
    safari = get_object_or_404(Buses, pk=pk)
    total_seats = 50  # Assuming the bus has 50 seats, adjust this as needed
    current_passengers = safari.passenger.all()  # Get the passengers who have booked
    available_seats = total_seats - current_passengers.count()

    if request.method == "POST":
        # Get the selected passenger ID from the POST data
        passenger_id = request.POST.get("passenger_id")
        if passenger_id:  # Check if a passenger is selected
            try:
                # Fetch the passenger or return a 404 if not found
                passenger = get_object_or_404(Passenger, pk=passenger_id)
                # Add the selected passenger to the bus
                safari.passenger.add(passenger)
                # Re-fetch the bus after adding a new passenger to update the passenger list
                safari = get_object_or_404(Buses, pk=pk)
                current_passengers = safari.passenger.all()
                available_seats = total_seats - current_passengers.count()
            except Passenger.DoesNotExist:
                # Handle the case where the passenger is not found (optional)
                pass

    # Pass the updated data to the template for rendering
    return render(request, "buses/book.html", {
        "safari": safari,
        "passengers": Passenger.objects.all(),  # All passengers to select from
        "current_passengers": current_passengers,  # Current passengers on the bus
        "available_seats": available_seats  # Available seats after booking
    })
