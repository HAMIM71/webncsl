from django.shortcuts import render, get_object_or_404
from .models import Service, Partner, News


def home(request):
    services = Service.objects.filter(is_active=True)
    partners = Partner.objects.filter(is_active=True)
    news_list = News.objects.filter(is_published=True).order_by('-published_at')[:3]
    return render(request, 'main/index.html', {
        'services': services,
        'partners': partners,
        'news_list': news_list,
    })


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    
    # Get related services (excluding current service)
    # Using random order to show different services each time
    related_services = Service.objects.filter(is_active=True).exclude(id=service.id).order_by('?')[:3]
    
    return render(request, 'main/service_detail.html', {
        'service': service,
        'related_services': related_services,
    })


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, is_published=True)
    
    # Get related news articles (excluding current article)
    # Ordered by most recent, limited to 3 articles
    related_news = News.objects.filter(is_published=True).exclude(id=news.id).order_by('-published_at')[:3]
    
    return render(request, 'main/news_detail.html', {
        'news': news,
        'related_news': related_news,
    })