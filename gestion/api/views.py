from email import message
from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
import json, requests
import uuid
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render,reverse
from django.http import HttpResponse
from api.forms import UserRegistration,CostumerRegistration, UpdateProfile, UpdatePasswords, SaveCategory, SaveLocation, SaveBus, SaveSchedule, SaveBooking, PayBooked
from api.models import Booking, Category, Location, Bus, Schedule, Paiement 
from cryptography.fernet import Fernet
from django.conf import settings
import base64
from datetime import datetime
from django.db.models import Q
from django.http import JsonResponse
from .models import Schedule
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils import formats
from django.shortcuts import render, get_object_or_404
from .models import Booking
from django.core.exceptions import ObjectDoesNotExist
from .serializers import ScheduleSerializers
from  rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from reportlab.pdfgen import canvas
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.conf import settings
import os
class SchedulerViewSet(viewsets.ModelViewSet):
    
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializers


context = {
    'page_title' : 'service gestion',
}



from django.contrib.auth.decorators import login_required

@login_required(login_url='/')

@login_required
def register_admin(request):
    user = request.user
    context = {}
    context['page_title'] = "Register User"
    if request.method == 'POST':
        data = request.POST
        form = UserRegistration(data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            
            try:
                # Vérifie si l'utilisateur existe déjà
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # L'utilisateur n'existe pas, crée un nouveau superutilisateur
                user = User.objects.create_superuser(username=username, password=pwd)
            else:
                # L'utilisateur existe déjà, met à jour ses droits de superutilisateur
                user.is_superuser = True
                user.set_password(pwd)
                user.save()
            
            loginUser = authenticate(username=username, password=pwd)
            
            login(request, loginUser)

            return redirect('home-page')
        else:
            context['reg_form'] = form
    return render(request, 'register_admin.html', context)

def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active and user.is_superuser:
                login(request, user)
                return redirect('home-page')
            else:
                messages.error(request, "Vous n'êtes pas autorisé à accéder à cette page.")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, 'login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('/')

@api_view(['GET'])
def gestion(request):
    return redirect('/')

@login_required
def home(request):
    context['page_title'] = 'Home'
    context['buses'] = Bus.objects.count()
    context['categories'] = Category.objects.count()
    context['upcoming_trip'] = Schedule.objects.filter(status= 1, schedule__gt = datetime.today()).count()
    
    return render(request, 'home.html',context)

@login_required
def register_admin(request):
    user = request.user
    context = {}
    context['page_title'] = "Register User"
    if request.method == 'POST':
        data = request.POST
        form = UserRegistration(data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            
            try:
                # Vérifie si l'utilisateur existe déjà
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # L'utilisateur n'existe pas, crée un nouveau superutilisateur
                user = User.objects.create_superuser(username=username, password=pwd)
            else:
                # L'utilisateur existe déjà, met à jour ses droits de superutilisateur
                user.is_superuser = True
                user.set_password(pwd)
                user.save()
            
            loginUser = authenticate(username=username, password=pwd)
            
            login(request, loginUser)

            return redirect('home-page')
        else:
            context['reg_form'] = form
    return render(request, 'register_admin.html', context)

login_required
def register_User(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home-page')
    context['page_title'] = "Register User"
    if request.method == 'POST':
        data = request.POST
        form = UserRegistration(data)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            loginUser = authenticate(username= username, password = pwd)
            login(request, loginUser)
            return redirect('home-page')
        else:
            context['reg_form'] = form

    return render(request,'register.html',context)

@login_required
def update_profile(request):
    context['page_title'] = 'Update Profile'
    user = User.objects.get(id = request.user.id)
    if not request.method == 'POST':
        form = UpdateProfile(instance=user)
        context['form'] = form
        print(form)
    else:
        form = UpdateProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated")
            return redirect("profile")
        else:
            context['form'] = form
            
    return render(request, 'manage_profile.html',context)


@login_required
def update_password(request):
    context['page_title'] = "Update Password"
    if request.method == 'POST':
        form = UpdatePasswords(user = request.user, data= request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Account Password has been updated successfully")
            update_session_auth_hash(request, form.user)
            return redirect("profile")
        else:
            context['form'] = form
    else:
        form = UpdatePasswords(request.POST)
        context['form'] = form
    return render(request,'update_password.html',context)


@login_required
def profile(request):
    context['page_title'] = 'Profile'
    return render(request, 'profile.html',context)

#contact_form

@login_required
def contact(request):
    return render(request, 'contact.html',context)

# Category
@login_required
def category_mgt(request):
    context['page_title'] = "Bus Categories"
    categories = Category.objects.all()
    context['categories'] = categories

    return render(request, 'category_mgt.html', context)

@login_required
def save_category(request):
    resp = {'status':'failed','msg':''}
    if request.method == 'POST':
        if (request.POST['id']).isnumeric():
            category = Category.objects.get(pk=request.POST['id'])
        else:
            category = None
        if category is None:
            form = SaveCategory(request.POST)
        else:
            form = SaveCategory(request.POST, instance= category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category has been saved successfully.')
            resp['status'] = 'success'
        else:
            for fields in form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")
    else:
        resp['msg'] = 'No data has been sent.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@login_required
def manage_category(request, pk=None):
    context['page_title'] = "Manage Category"
    if not pk is None:
        category = Category.objects.get(id = pk)
        context['category'] = category
    else:
        context['category'] = {}

    return render(request, 'manage_category.html', context)

@login_required
def delete_category(request):
    resp = {'status':'failed', 'msg':''}

    if request.method == 'POST':
        try:
            category = Category.objects.get(id = request.POST['id'])
            category.delete()
            messages.success(request, 'Category has been deleted successfully')
            resp['status'] = 'success'
        except Exception as err:
            resp['msg'] = 'Category has failed to delete'
            print(err)

    else:
        resp['msg'] = 'Category has failed to delete'
    
    return HttpResponse(json.dumps(resp), content_type="application/json")

# Location
@login_required
def location_mgt(request):
    context['page_title'] = "Locations"
    locations = Location.objects.all()
    context['locations'] = locations

    return render(request, 'location_mgt.html', context)

@login_required
def save_location(request):
    resp = {'status':'failed','msg':''}
    if request.method == 'POST':
        if (request.POST['id']).isnumeric():
            location = Location.objects.get(pk=request.POST['id'])
        else:
            location = None
        if location is None:
            form = SaveLocation(request.POST)
        else:
            form = SaveLocation(request.POST, instance= location)
        if form.is_valid():
            form.save()
            messages.success(request, 'Location has been saved successfully.')
            resp['status'] = 'success'
        else:
            for fields in form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")
    else:
        resp['msg'] = 'No data has been sent.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@login_required
def manage_location(request, pk=None):
    context['page_title'] = "Manage Location"
    if not pk is None:
        location = Location.objects.get(id = pk)
        context['location'] = location
    else:
        context['location'] = {}

    return render(request, 'manage_location.html', context)

@login_required
def delete_location(request):
    resp = {'status':'failed', 'msg':''}

    if request.method == 'POST':
        try:
            location = Location.objects.get(id = request.POST['id'])
            location.delete()
            messages.success(request, 'Location has been deleted successfully')
            resp['status'] = 'success'
        except Exception as err:
            resp['msg'] = 'location has failed to delete'
            print(err)

    else:
        resp['msg'] = 'location has failed to delete'
    
    return HttpResponse(json.dumps(resp), content_type="application/json")


# bus
@login_required
def bus_mgt(request):
    context['page_title'] = "Buses"
    buses = Bus.objects.all()
    context['buses'] = buses

    return render(request, 'bus_mgt.html', context)

@login_required
def save_bus(request):
    resp = {'status':'failed','msg':''}
    if request.method == 'POST':
        if (request.POST['id']).isnumeric():
            bus = Bus.objects.get(pk=request.POST['id'])
        else:
            bus = None
        if bus is None:
            form = SaveBus(request.POST)
        else:
            form = SaveBus(request.POST, instance= bus)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bus has been saved successfully.')
            resp['status'] = 'success'
        else:
            for fields in form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")
    else:
        resp['msg'] = 'No data has been sent.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@login_required
def manage_bus(request, pk=None):
    context['page_title'] = "Manage Bus"
    categories = Category.objects.filter(status = 1).all()
    context['categories'] = categories
    if not pk is None:
        bus = Bus.objects.get(id = pk)
        context['bus'] = bus
    else:
        context['bus'] = {}

    return render(request, 'manage_bus.html', context)

@login_required
def delete_bus(request):
    resp = {'status':'failed', 'msg':''}

    if request.method == 'POST':
        try:
            bus = Bus.objects.get(id = request.POST['id'])
            bus.delete()
            messages.success(request, 'Bus has been deleted successfully')
            resp['status'] = 'success'
        except Exception as err:
            resp['msg'] = 'bus has failed to delete'
            print(err)

    else:
        resp['msg'] = 'bus has failed to delete'
    
    return HttpResponse(json.dumps(resp), content_type="application/json")    


# schedule
@login_required
def schedule_mgt(request):
    context['page_title'] = "Trip Schedules"
    schedules = Schedule.objects.all()
    context['schedules'] = schedules

    return render(request, 'schedule_mgt.html', context)

@login_required
def save_schedule(request):
    resp = {'status':'failed','msg':''}
    if request.method == 'POST':
        if (request.POST['id']).isnumeric():
            schedule = Schedule.objects.get(pk=request.POST['id'])
        else:
            schedule = None
        if schedule is None:
            form = SaveSchedule(request.POST)
        else:
            form = SaveSchedule(request.POST, instance= schedule)
        if form.is_valid():
            form.save()
            messages.success(request, 'Schedule has been saved successfully.')
            resp['status'] = 'success'
        else:
            for fields in form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")
    else:
        resp['msg'] = 'No data has been sent.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@login_required
def manage_schedule(request, pk=None):
    context['page_title'] = "Manage Schedule"
    buses = Bus.objects.filter(status = 1).all()
    locations = Location.objects.filter(status = 1).all()
    context['buses'] = buses
    context['locations'] = locations
    if not pk is None:
        schedule = Schedule.objects.get(id = pk)
        context['schedule'] = schedule
    else:
        context['schedule'] = {}

    return render(request, 'manage_schedule.html', context)

login_required
def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'customer_home.html', {'schedules': schedules})

@login_required
def delete_schedule(request):
    resp = {'status':'failed', 'msg':''}

    if request.method == 'POST':
        try:
            schedule = Schedule.objects.get(id = request.POST['id'])
            schedule.delete()
            messages.success(request, 'Schedule has been deleted successfully')
            resp['status'] = 'success'
        except Exception as err:
            resp['msg'] = 'schedule has failed to delete'
            print(err)

    else:
        resp['msg'] = 'Schedule has failed to delete'
    
    return HttpResponse(json.dumps(resp), content_type="application/json")  


# scheduled Trips
@login_required
def scheduled_trips(request):
    if not request.method == 'POST':
        context['page_title'] = "Scheduled Trips"
        schedules = Schedule.objects.filter(status = 1, schedule__gt = datetime.now()).all()
        context['schedules'] = schedules
        context['is_searched'] = False
        context['data'] = {}
    else:
        context['page_title'] = "Search Result | Scheduled Trips"
        context['is_searched'] = True
        date = datetime.strptime(request.POST['date'],"%Y-%m-%d").date()
        year = date.strftime('%Y')
        month = date.strftime('%m')
        day = date.strftime('%d')
        depart = Location.objects.get(id = request.POST['depart'])
        destination = Location.objects.get(id = request.POST['destination'])
        schedules = Schedule.objects.filter(Q(status = 1) & Q(schedule__year = year) & Q(schedule__month = month) & Q(schedule__day = day) & Q(Q(depart = depart) | Q(destination = destination ))).all()
        context['schedules'] = schedules
        context['data'] = {'date':date,'depart':depart, 'destination': destination}

    return render(request, 'scheduled_trips.html', context)

@login_required
def manage_booking(request, schedPK=None, pk=None):
    context['page_title'] = "Manage Booking"
    context['schedPK'] = schedPK
    if not schedPK is None:
        schedule = Schedule.objects.get(id = schedPK)
        context['schedule'] = schedule
    else:
        context['schedule'] = {}
    if not pk is None:
        book = Booking.objects.get(id = pk)
        context['book'] = book
    else:
        context['book'] = {}

    return render(request, 'manage_book.html', context)

@login_required
def save_booking(request):
    resp = {'status':'failed','msg':''}
    if request.method == 'POST':
        if (request.POST['id']).isnumeric():
            booking = Booking.objects.get(pk=request.POST['id'])
        else:
            booking = None
        if booking is None:
            form = SaveBooking(request.POST)
        else:
            form = SaveBooking(request.POST, instance= booking)
        if form.is_valid():
            form.save()
            if booking is None:
                booking = Booking.objects.last()
                messages.success(request, f'Booking has been saved successfully. Your Booking Refderence Code is: <b>{booking.code}</b>', extra_tags = 'stay')
            else:
                messages.success(request, f'<b>{booking.code}</b> Booking has been updated successfully.')
            resp['status'] = 'success'
        else:
            for fields in form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")
    else:
        resp['msg'] = 'No data has been sent.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

# login_required
# def bookings(request):
#     context['page_title'] = "Bookings"
    
    
    
    
#     bookings = Booking.objects.all()
#     context['bookings'] = bookings

#     return render(request, 'bookings.html', context)
@login_required
def bookings(request):
    try:
        url = 'http://msreservation:8003/api/Booking/'
        
        response = requests.get(url)
        
        if response.status_code == 200:
            dataToSave = response.json()
            
            for elt in dataToSave:
                booking = Booking.objects.create(
                    id=elt['id'],
                    code=elt['code'],
                    name=elt['name'],
                    seats=elt['seats'],
                    status=elt['status']
                )
                
                schedule_id = elt['schedule']
                schedule_location = Location.objects.get(id=schedule_id)
                booking.schedule = schedule_location
                booking.save()
                
            bookings = Booking.objects.all()
            return render(request, 'bookings.html', {'bookings': bookings})
    except ConnectionError:
        pass
    return render(request, 'error.html')

@login_required
def view_booking(request,pk=None):
    if pk is None:
        messages.error(request, "Unkown Booking ID")
        return redirect('booking-page')
    else:
        context['page_title'] = 'Vieww Booking'
        context['booking'] = Booking.objects.get(id = pk)
        return render(request, 'view_booked.html', context)


@login_required
def pay_booked(request):
    resp = {'status':'failed','msg':''}
    if not request.method == 'POST':
        resp['msg'] = "Unknown Booked ID"
    else:
        booking = Booking.objects.get(id= request.POST['id'])
        form = PayBooked(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, f"<b>{booking.code}</b> has been paid successfully", extra_tags='stay')
            resp['status'] = 'success'
        else:
            for field in form:
                for error in field.errors:
                    resp['msg'] += str(error + "<br>")
    
    return HttpResponse(json.dumps(resp),content_type = 'application/json')

@login_required
def delete_booking(request):
    resp = {'status':'failed', 'msg':''}

    if request.method == 'POST':
        try:
            booking = Booking.objects.get(id = request.POST['id'])
            code = booking.code
            booking.delete()
            messages.success(request, f'[<b>{code}</b>] Booking has been deleted successfully')
            resp['status'] = 'success'
        except Exception as err:
            resp['msg'] = 'booking has failed to delete'
            print(err)

    else:
        resp['msg'] = 'booking has failed to delete'
    
    return HttpResponse(json.dumps(resp), content_type="application/json")  
login_required
def find_trip(request):
    context['page_title'] = 'Find Trip Schedule'
    context['locations'] = Location.objects.filter(status = 1).all
    today = datetime.today().strftime("%Y-%m-%d")
    context['today'] = today
    return render(request, 'find_trip.html', context)

login_required
def formulaire_view(request):
    if request.method == 'POST':

        nom = request.POST.get('nom')
        schedule_id = request.POST.get('schedule')
        try:
            # Check if the Schedule object with the specified ID exists
            schedule = Schedule.objects.get(id=schedule_id)
            schedule_id = schedule.id
            if Schedule.objects.filter(pk=schedule_id).exists():
                # Retrieve the Schedule object
                schedule = Schedule.objects.get(pk=schedule_id)

                # Perform the remaining logic
                seats_available = schedule.nbrePlace()
                booking = Booking(
                name=nom,
                schedule=schedule,
                seats=min(2, seats_available),  # Ajuster le nombre de sièges en fonction des places disponibles
                status='1'  # Vous pouvez également définir le statut par défaut ici
                )
                booking.code = str(uuid.uuid4())[:6].upper()  # Générer un code unique de 6 caractères
                # Sauvegarder la réservation dans la base de données
                if not booking.pk:
                    last_booking = Booking.objects.order_by('-seats').first()
                    if last_booking:
                        if last_booking.seats < seats_available:
                            booking.seats = last_booking.seats + 1
                        else:
                            return HttpResponse('bus complete')
                    else:
                        booking.seats = 1
                booking.save()
                
                id = booking.id
                
                # Generate the dynamic URL using the booking ID
                url = reverse('formulaire_paiement', kwargs={'booking_id': id})
                
                return redirect(url)
            
            else:
                # Handle the case when the Schedule object does not exist
                return HttpResponse('Schedule does not exist.')

        except ObjectDoesNotExist:
            # Handle the case when there is an ObjectDoesNotExist exception
            return HttpResponse('Schedule does not exist.')

    return render(request, 'formulaire2.html')

@login_required

def get_schedules(request):
    schedules = Schedule.objects.all()
    data = [
        {
            'id': schedule.id,
            'code': schedule.code,
            'depart': schedule.depart.location,  # Utilisez la propriété location de votre modèle Location
            'destination': schedule.destination.location,  # Utilisez la propriété location de votre modèle Location
            'horaire': schedule.schedule
        }
        for schedule in schedules
    ]
    return JsonResponse(data, safe=False)

@login_required
def reservation_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'reservation_detail.html', {'booking': booking})

@login_required
def download_pdf(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Replace 'pdfs' with the actual directory where you store your PDFs
    pdf_directory = 'pdfs'
    pdf_path = os.path.join(settings.BASE_DIR, pdf_directory, f'reservation_{booking.code}.pdf')

    # Make sure the file exists before trying to serve it
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            response = FileResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename=reservation_{booking.code}.pdf'
            return response

    else:
        # Handle the case when the file doesn't exist
        print(f"pdf_path: {booking}")

        return HttpResponse("PDF not found", status=404)


@login_required
def generate_pdf(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=reservation_{booking.code}.pdf'

    p = canvas.Canvas(response)

    p.setStrokeColorRGB(0, 0, 1)
    p.setFillColorRGB(0.9, 0.9, 1)
    p.roundRect(50, 200, 500, 300, 20, fill=1)

    p.setFont("Helvetica", 12)
    p.setFillColorRGB(0, 0, 0)

    text_width = p.stringWidth(f"Ticket ", "Helvetica", 12)
    x_position = (550 - text_width) / 2

    p.drawString(x_position, 450, f"Ticket ")
    p.drawString(100, 400, f"Nom: {booking.name}")

    horaire_str = formats.date_format(booking.schedule.schedule, "DATETIME_FORMAT")

    p.drawString(100, 375, f"Horaire: {horaire_str}")    
    p.drawString(100, 350, f"Bus number: {booking.schedule.bus.bus_number}")
    
    p.drawString(100, 325, f"Bus Category: {booking.schedule.bus.category}")
    p.drawString(100, 300, f"Seat number: {booking.seats}")
    p.drawString(100, 275, f"trajet: {booking.schedule.depart}-{booking.schedule.destination}")

    p.drawString(100, 250, f"Amount Payable: {intcomma(booking.schedule.fare)}")
    p.drawString(100, 225, f"Statut: {'Pending' if booking.status == '1' else 'Paid'}")

    # Ajoutez le bouton de téléchargement
    p.setFont("Helvetica-Bold", 12)
    p.setFillColorRGB(0, 0, 1)  # Couleur bleue pour le lien
    # p.drawString(100, 50, "Télécharger")
    # p.linkURL(reverse('download_pdf', args=[booking.id]), (100, 50, 200, 65))

    # Ajoutez le bouton de retour
    p.setFont("Helvetica-Bold", 12)
    p.setFillColorRGB(0, 0, 1)  # Couleur bleue pour le lien
    p.drawString(300, 50, "Retour")
    p.linkURL(reverse('booking-page'), (300, 50, 400, 65))

    p.showPage()
    p.save()

    return response


