from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.contrib import messages
from .models import ShortenedURL
import validators

def home(request):
    if request.method == 'POST':
        original_url = request.POST.get('url', '').strip()
        
        # Validate URL
        if not original_url:
            messages.error(request, 'Please enter a URL')
            return render(request, 'shortener/home.html')
        
        # Add http:// if missing
        if not original_url.startswith(('http://', 'https://')):
            original_url = 'https://' + original_url
        
        # Validate URL format
        if not validators.url(original_url):
            messages.error(request, 'Please enter a valid URL')
            return render(request, 'shortener/home.html')
        
        # Check if URL already exists
        existing = ShortenedURL.objects.filter(original_url=original_url).first()
        if existing:
            shortened_url = request.build_absolute_uri(reverse('redirect_url', args=[existing.short_code]))
            messages.success(request, f'URL already exists: {shortened_url}')
            return render(request, 'shortener/home.html', {
                'shortened_url': shortened_url,
                'original_url': original_url
            })
        
        # Create new shortened URL
        short_url_obj = ShortenedURL.objects.create(original_url=original_url)
        shortened_url = request.build_absolute_uri(reverse('redirect_url', args=[short_url_obj.short_code]))
        
        messages.success(request, 'URL shortened successfully!')
        return render(request, 'shortener/home.html', {
            'shortened_url': shortened_url,
            'original_url': original_url
        })
    
    return render(request, 'shortener/home.html')

def redirect_url(request, short_code):
    url_obj = get_object_or_404(ShortenedURL, short_code=short_code)
    url_obj.click_count += 1
    url_obj.save()
    return redirect(url_obj.original_url)

def analytics(request):
    urls = ShortenedURL.objects.all().order_by('-created_at')[:50]
    return render(request, 'shortener/analytics.html', {'urls': urls})