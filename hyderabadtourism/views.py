from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def mallikarjun_tours(request):
    return render(request,'mallikarjun-tours.html')

def pay_online(request):
    return render(request,'pay-online.html')

def contact(request):
    return render(request,'contact.html')

def about_hyderabad(request):
    return render(request,'about-hyderabad.html')

def sight_seeing(request):
    return render(request,'sight-seeing.html')

def special_attractions(request):
    return render(request,'special-attractions.html')

def hyderabad_city_tour(request):
    return render(request,'hyderabad-city-tour.html')

def ramoji_film_city_tour(request):
    return render(request,'ramoji-film-city-tour.html')

def charminar(request):
    return render(request,'charminar.html')

def golconda(request):
    return render(request,'golconda.html')

def hussain_sagar(request):
    return render(request,'hussain-sagar.html')

def about_us(request):
    return render(request,'about-us.html')

def services(request):
    return render(request,'services.html')

def achievements(request):
    return render(request,'achievements.html')

def terms_and_conditions(request):
    return render(request,'terms-and-conditions.html')

def privacy_policy(request):
    return render(request,'privacy-policy.html')

def desclaimer(request):
    return render(request,'desclaimer.html')

def returns_and_refunds(request):
    return render(request,'returns-and-refunds.html')