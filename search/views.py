from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .forms import *
from user_profile.models import UserProfile

@csrf_protect
@login_required
def searchUsers(request):
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            users = UserProfile.objects.filter(fullName__icontains=cd['name'])
            return render(request, 'search/user_search_results.html', {'searchedName' : cd['name'], 'users' : users})
    else:
        form = UserSearchForm()
    return render(request, 'search/search_user.html', {'form' : form})
