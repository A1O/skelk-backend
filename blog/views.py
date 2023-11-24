from django.shortcuts import render, redirect
from .models import Profile, Blog
from .forms import BlogForm


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def dashboard(request):
    form = BlogForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect("blog:dashboard")
    followed_blogs = Blog.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by('-created_at')
    return render(request, 'blog/dashboard.html', {"form": form, "blogs": followed_blogs})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user.id)
    return render(request, 'blog/profile_list.html', {'profiles': profiles})


def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, 'blog/profile.html', {'profile': profile})
