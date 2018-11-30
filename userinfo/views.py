from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

from .forms import UserForm, ProfileForm
from .models import District, SubDistrict, Union, Village

# Create your views here.

def profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            email = user_form.cleaned_data["email"]
            password = user_form.cleaned_data["password"]
            re_password = user_form.cleaned_data["re_password"]
            if password == re_password:
            	try:
            		user = User.objects.create_user(username=email, email=email, password=password)
            	except:
            		return HttpResponse('Failed! Try again.')
            profile = profile_form.save(commit=False)
            profile.user = user
            if profile.dis_pro == True:
            	profile.subdis_pro = True
            	profile.uni_pro = True
            	profile.vil_pro = True
            elif profile.subdis_pro == True:
            	profile.uni_pro = True
            	profile.vil_pro = True
            elif profile.uni_pro ==True:
            	profile.vil_pro = True
            profile.save()
            return HttpResponse('Create successfully.')
        else:
            return HttpResponse('Please correct the error below.')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    template = 'userinfo/profile_create.html'

    context = {
    	'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, template, context)


def load_subdistrict(request):
    district_id = request.GET.get('district')
    sub = SubDistrict.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'userinfo/dropdown_list_options.html', {'sub': sub})

def load_union(request):
    subdistrict_id = request.GET.get('subdistrict')
    uni = Union.objects.filter(subdistrict_id=subdistrict_id).order_by('name')
    return render(request, 'userinfo/dropdown_list_options.html', {'uni': uni})

def load_village(request):
    union_id = request.GET.get('union')
    vil = Village.objects.filter(union_id=union_id).order_by('name')
    return render(request, 'userinfo/dropdown_list_options.html', {'vil': vil})