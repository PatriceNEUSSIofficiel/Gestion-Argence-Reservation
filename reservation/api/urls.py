from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from .views import formulaire_view
from .views import get_schedules
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import reservation_detail, generate_pdf, BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Booking',BookingViewSet)
router.register(r'Booking',BookingViewSet)

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('',views.init,name='init-page'),
    path('init',views.init,name='init'),
    path('welcome',views.welcome,name='welcome-page'),
    path('home',views.home,name='home-page'),
    path('costumer_home',views.schedule_list,name='schedule-list'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name='login'),    
    path('user-login', views.login_user, name="login-user"),
    path('user-register', views.register_User, name="register-user"),
    path('admin-login', views.login_admin, name="login-admin"),
    path('admin-register', views.register_admin, name="register-admin"),
    path('logout',views.logoutuser,name='logout'),
    path('profile',views.profile,name='profile'),
    path('update-profile',views.update_profile,name='update-profile'),
    path('update-password',views.update_password,name='update-password'),
    path('online_booking',views.save_booking,name='online-book'),
    path('veiw_booking/<int:pk>',views.view_booking,name='veiw-booking'),
    path('find_trip',views.find_trip,name='find-trip-page'),
    path('formulaire2/', formulaire_view, name='formulaire2'),
    path('get_schedules/', get_schedules, name='get_schedules'),
    path('reservation_detail/<int:booking_id>/', views.reservation_detail, name='reservation_detail'),    
    path('generate_pdf/<int:booking_id>/', generate_pdf, name='generate_pdf'),
    path('contact/', views.send_email, name='contact'),
    path('formulaire_paiement/<int:booking_id>/', views.formulaire_paiement, name='formulaire_paiement'),
    path('map/', views.map, name='map'),
    path('gestions/', views.gestions, name='gestions'),
    path('route/', views.route, name='route'),
    path('api/', include(router.urls)),



    
]
