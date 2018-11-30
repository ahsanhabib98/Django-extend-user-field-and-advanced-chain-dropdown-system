from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, SubDistrict, Union, Village

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user', 'is_user', 'is_editor')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subdistrict'].queryset = SubDistrict.objects.none()
        self.fields['union'].queryset = Union.objects.none()
        self.fields['village'].queryset = Village.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['subdistrict'].queryset = SubDistrict.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subdistrict'].queryset = self.instance.district.subdistrict_set.order_by('name')

        if 'subdistrict' in self.data:
            try:
                subdistrict_id = int(self.data.get('subdistrict'))
                self.fields['union'].queryset = Union.objects.filter(subdistrict_id=subdistrict_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
        	self.fields['union'].queryset = self.instance.subdistrict.union_set.order_by('name')

        if 'union' in self.data:
            try:
                union_id = int(self.data.get('union'))
                self.fields['village'].queryset = Village.objects.filter(union_id=union_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['village'].queryset = self.instance.union.village_set.order_by('name')