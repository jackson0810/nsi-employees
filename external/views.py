from django.shortcuts import render

from .models import NewsItem, FunctionalCapability, ImageItem


def home(request):
    latest_news = NewsItem.objects.filter(featured=True)
    featured_images = ImageItem.objects.filter(featured=True)

    return render(request, 'home.html', {'latest_news': latest_news, 'featured_images': featured_images})


def about_us(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def clients_partners(request):
    return render(request, 'clients_partners.html')


def china_lake(request):
    return render(request, 'locations/china_lake.html')


def seaporte(request):
    func_capabilities = FunctionalCapability.objects.all()

    return render(request, 'contract_vehicles/seaport-e.html', {'func_capabilities': func_capabilities})


def careers(request):
    return render(request, 'careers.html')


def news(request):
    return render(request, 'news.html')
