from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
#
from .views import formulaire_view
from .views import get_schedules

###########################


from django.urls import path
from .views import reservation_detail, generate_pdf

####################""
urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('home',views.home,name='home-page'),
    path('costumer_home',views.schedule_list,name='schedule-list'),
    path('', auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name='login'),    
    path('user-login', views.login_user, name="login-user"),
    path('user-register', views.register_User, name="register-user"),
    path('logout',views.logoutuser,name='logout'),
    path('profile',views.profile,name='profile'),
    path('update-profile',views.update_profile,name='update-profile'),
    path('update-password',views.update_password,name='update-password'),  
    path('contact/', views.contact, name='contact'),
    path('route', views.route, name="route"),
    path('geolocalisation', views.geolocalisation, name="geolocalisation"),
    path('map', views.map, name="map"),
    
]
