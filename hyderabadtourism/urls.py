"""
URL configuration for hyderabadtourism project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hyderabadtourism import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('mallikarjun-tours',views.mallikarjun_tours,name='mallikarjun-tours'),
    path('pay-online',views.pay_online,name='pay-online'),
    path('contact',views.contact,name='contact'),
    path('about-hyderabad',views.about_hyderabad,name='about-hyderabad'),
    path('sight-seeing',views.sight_seeing,name='sight-seeing'),
    path('special-attractions',views.special_attractions,name='special-attractions'),
    path('hyderabad-city-tour',views.hyderabad_city_tour,name='hyderabad-city-tour'),
    path('ramoji-film-city-tour',views.ramoji_film_city_tour,name='ramoji-film-city-tour'),
    path('hussain-sagar',views.hussain_sagar,name='hussain-sagar'),
    path('charminar',views.charminar,name='charminar'),
    path('golconda',views.golconda,name='golconda'),
    path('about-us',views.about_us,name='about-us'),
    path('services',views.services,name='services'),
    path('achievements',views.achievements,name='achievements'),
    path('terms-and-conditions',views.terms_and_conditions,name='terms-and-conditions'),
    path('privacy-policy',views.privacy_policy,name='privacy-policy'),
    path('desclaimer',views.desclaimer,name='desclaimer'),
    path('returns-and-refunds',views.returns_and_refunds,name='returns-and-refunds'),
]
