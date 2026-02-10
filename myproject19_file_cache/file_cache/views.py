from django.shortcuts import render
from django.shortcuts import render
from .models import YouTubeUser
from django.core.cache import cache

def user_list(request):
    users = cache.get('users_data')
    if users is None:
        print("Cache miss: Fetching data from database")
        users = YouTubeUser.objects.all()
        cache.set('users_data', users) # Cache data for 60 seconds
    else:
        print("Cache hit: Fetching data from cache")

    return render(request, 'file_cache/users_list.html', {'users': users})
