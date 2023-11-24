from django.shortcuts import render
from .models import Profile


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def dashboard(request):
    return render(request, 'base.html')


def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'blog/profile_list.html', {'profiles': profiles})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, 'blog/profile.html', {'profile': profile})
