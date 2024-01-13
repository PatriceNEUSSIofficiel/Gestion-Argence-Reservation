import sched
from unicodedata import category
from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm, UserChangeForm

from django.contrib.auth.models import User
from more_itertools import quantify
from .models import Category, Location, Bus, Schedule, Booking, Email
from datetime import datetime

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['sender', 'receiver', 'subject', 'body']

class UserRegistration(UserCreationForm):
    email = forms.EmailField(max_length=250,help_text="The email field is required.")
    first_name = forms.CharField(max_length=250,help_text="The First Name field is required.")
    last_name = forms.CharField(max_length=250,help_text="The Last Name field is required.")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')
    

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email = email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"The {user.email} mail is already exists/taken")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username = username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"The {user.username} mail is already exists/taken")




class CostumerRegistration(UserCreationForm):
    email = forms.EmailField(max_length=250,help_text="The email field is required.")
    first_name = forms.CharField(max_length=250,help_text="The First Name field is required.")
    last_name = forms.CharField(max_length=250,help_text="The Last Name field is required.")
    cni = forms.CharField(max_length=250,help_text="The Last Name field is required.")

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name')
    

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email = email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"The {user.email} mail is already exists/taken")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username = username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"The {user.username} mail is already exists/taken")


class UpdateProfile(UserChangeForm):
    username = forms.CharField(max_length=250,help_text="The Username field is required.")
    email = forms.EmailField(max_length=250,help_text="The Email field is required.")
    first_name = forms.CharField(max_length=250,help_text="The First Name field is required.")
    last_name = forms.CharField(max_length=250,help_text="The Last Name field is required.")
    current_password = forms.CharField(max_length=250)

    class Meta:
        model = User
        fields = ('email', 'username','first_name', 'last_name')

    def clean_current_password(self):
        if not self.instance.check_password(self.cleaned_data['current_password']):
            raise forms.ValidationError(f"Password is Incorrect")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(email = email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"The {user.email} mail is already exists/taken")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(username = username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"The {user.username} mail is already exists/taken")

class UpdatePasswords(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="Old Password")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="Confirm New Password")
    class Meta:
        model = User
        fields = ('old_password','new_password1', 'new_password2')

class SaveCategory(forms.ModelForm):
    name = forms.CharField(max_length="250")
    description = forms.Textarea()
    status = forms.ChoiceField(choices=[('1','Active'),('2','Inactive')])

    class Meta:
        model = Category
        fields = ('name','description','status')

    def clean_name(self):
        id = self.instance.id if self.instance.id else 0
        name = self.cleaned_data['name']
        # print(int(id) > 0)
        # raise forms.ValidationError(f"{name} Category Already Exists.")
        try:
            if int(id) > 0:
                category = Category.objects.exclude(id=id).get(name = name)
            else:
                category = Category.objects.get(name = name)
        except:
            return name
            # raise forms.ValidationError(f"{name} Category Already Exists.")
        raise forms.ValidationError(f"{name} Category Already Exists.")

class SaveLocation(forms.ModelForm):
    location = forms.CharField(max_length="250")
    status = forms.ChoiceField(choices=[('1','Active'),('2','Inactive')])

    class Meta:
        model = Location
        fields = ('location','status')

    def clean_location(self):
        id = self.instance.id if self.instance.id else 0
        location = self.cleaned_data['location']
        # print(int(id) > 0)
        try:
            if int(id) > 0:
                loc = Location.objects.exclude(id=id).get(location = location)
            else:
                loc = Location.objects.get(location = location)
        except:
            return location
            # raise forms.ValidationError(f"{location} Category Already Exists.")
        raise forms.ValidationError(f"{location} Location Already Exists.")

class SaveBus(forms.ModelForm):
    bus_number = forms.CharField(max_length="250")
    category = forms.CharField(max_length="250")
    seats = forms.CharField(max_length="250")
    status = forms.ChoiceField(choices=[('1','Active'),('2','Inactive')])

    class Meta:
        model = Bus
        fields = ('bus_number','category','status','seats')

    def clean_category(self):
        id = self.cleaned_data['category']
        try:
            category = Category.objects.get(id = id)
            return category
        except:
            raise forms.ValidationError(f"Invalid Category Already Exists.")
    
    def clean_bus_number(self):
        id = self.instance.id if self.instance.id else 0
        bus_number = self.cleaned_data['bus_number']
        # print(int(id) > 0)
        try:
            if int(id) > 0:
                bus = Bus.objects.exclude(id=id).get(bus_number = bus_number)
            else:
                bus = Bus.objects.get(bus_number = bus_number)
        except:
            return bus_number
            # raise forms.ValidationError(f"{bus_number} Category Already Exists.")
        raise forms.ValidationError(f"{bus_number} bus Already Exists.")

class SaveSchedule(forms.ModelForm):
    code = forms.CharField(max_length="250")
    bus = forms.IntegerField()
    depart = forms.IntegerField()
    destination = forms.IntegerField()
    fare = forms.FloatField(min_value=0,max_value=999999)
    schedule = forms.CharField(max_length="250")
    status = forms.ChoiceField(choices=[('1','Active'),('2','Cancelled')])

    class Meta:
        model = Schedule
        fields = ('code','bus','depart','destination','fare','schedule','status')
    def clean_code(self):
        id = self.instance.id if self.instance.id else 0
        if id > 0:
            try:
                schedule = Schedule.objects.get(id = id)
                return schedule.code
            except:
                code= ''
        else:
            code= ''
        pref = datetime.today().strftime('%Y%m%d')
        code = str(1).zfill(4)
        while True:
            sched = Schedule.objects.filter(code=str(pref + code)).count()
            if sched > 0:
                code = str(int(code) + 1).zfill(4)
            else:
                code = str(pref + code)
                break
        return code

    def clean_bus(self):
        bus_id = self.cleaned_data['bus']

        try:
            bus = Bus.objects.get(id=bus_id)
            return bus
        except:
            raise forms.ValidationError("Bus is not recognized.")
    
    def clean_depart(self):
        location_id = self.cleaned_data['depart']

        try:
            location = Location.objects.get(id=location_id)
            return location
        except:
            raise forms.ValidationError("Depart is not recognized.")
    
    def clean_destination(self):
        location_id = self.cleaned_data['destination']

        try:
            location = Location.objects.get(id=location_id)
            return location
        except:
            raise forms.ValidationError("Destination is not recognized.")

class SaveBooking(forms.ModelForm):
    code = forms.CharField(max_length="250")
    schedule = forms.CharField(max_length="250")
    name = forms.CharField(max_length="250")
    seats = forms.CharField(max_length="250")

    class Meta:
        model = Booking
        fields = ('code','schedule','name','seats')

    def clean_code(self):
        id = self.instance.id if self.instance.id else 0
        if id > 0:
            try:
                booking = Booking.objects.get(id = id)
                return booking.code
            except:
                code= ''
        else:
            code= ''
        pref = datetime.today().strftime('%Y%m%d')
        code = str(1).zfill(4)
        while True:
            sched = Booking.objects.filter(code=str(pref + code)).count()
            if sched > 0:
                code = str(int(code) + 1).zfill(4)
            else:
                code = str(pref + code)
                break
        print(code)
        return code

    def clean_schedule(self):
        schedule_id = self.cleaned_data['schedule']
        # print(int(id) > 0)
        try:
            sched = Schedule.objects.get(id = schedule_id)
            return sched
        except:
            raise forms.ValidationError(f"Trip Schedule is not recognized.")

class PayBooked(forms.ModelForm):
    status = forms.IntegerField()
    class Meta:
        model = Booking
        fields = ('status',)
