from django.contrib import admin
from django.urls import path
from food import views
from django.contrib.auth.views import LoginView, LogoutView

admin.site.site_header = "Zero Food Admin"
admin.site.site_title = "Zero Food Admin Portal"
admin.site.index_title = "Welcome to Zero Food Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view, name='home'),
    path('ngoclick/', views.ngoclick_view, name='ngoclick'),
    path('donarclick/', views.donarclick_view, name='donarclick'),
    path('ngosignup/', views.ngo_signup_view, name='ngosignup'),
    path('donarsignup/', views.donar_signup_view, name='donarsignup'),
    path('ngologin/', LoginView.as_view(template_name='ngologin.html'), name='ngologin'),
    path('donarlogin/', LoginView.as_view(template_name='donarlogin.html'), name='donarlogin'),
    path('afterlogin/', views.afterlogin_view, name='afterlogin'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='logout'),
    path('ngo-dashboard/', views.ngo_dashboard_view, name='ngo-dashboard'),
    path('ngo-donation/', views.ngo_donation_view, name='ngo-donation'),
    path('ngo-notice/', views.ngo_notice_view, name='ngo-notice'),
    path('claim-donation/<int:pk1>/<int:pk2>/<str:pk3>/', views.claim_donation_view, name='claim-donation'),
    path('donar-dashboard/', views.donar_dashboard_view, name='donar-dashboard'),
    path('donar-donation/', views.donar_donation_view, name='donar-donation'),
    path('claimed-donation/', views.claimed_donation_view, name='claimed-donation'),
    path('donar-donation-history/', views.donar_donation_history_view, name='donar-donation-history'),
    path('aboutus/', views.aboutus_view, name='aboutus'),
    path('contactus/', views.contactus_view, name='contactus'),
    path('claim_food/<int:pk1>/', views.claim_food, name='claim_food'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
