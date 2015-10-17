from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from user_profile.forms import *
from django.template import RequestContext
from user_profile.models import UserProfile
from django.http import HttpResponse
from django.contrib.auth.models import User

@login_required
def view_profile(request, username=None):
    selfProfile = True
    if username is not None:
        selfProfile = False
        try:
            user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            return HttpResponseRedirect('/home/')
    else:
        user = request.user
    try:
        user_profile = user.profile
    except UserProfile.DoesNotExist():
        return create_profile(request)
    variables = RequestContext(request, {'userprofile' : user_profile, 'selfProfile' : selfProfile})
    return render_to_response('user_profile/profile.html', variables, )

@csrf_protect
@login_required
def create_profile(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist():
        profile = UserProfile(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user_profile = profile
            user_profile.user = request.user
            user_profile.fullName = form.cleaned_data['fullName']
            user_profile.phoneNumber = form.cleaned_data['phoneNumber']
            user_profile.website = form.cleaned_data['website']
            user_profile.save()
            return HttpResponseRedirect('../view')
    else:
        form = ProfileForm(initial={'fullName':profile.fullName, 'phoneNumber':profile.phoneNumber, 'website':profile.website})
    variables = RequestContext(request, {'form' : form})
    return render_to_response('user_profile/create_profile.html', variables, )
