from django.urls import path
from django.contrib.auth import views as auth_views
from .views import profile, load_subdistrict, load_union, load_village


urlpatterns = [

    path('registration/', profile, name='register'),
    path('hr/ajax/load-sub/', load_subdistrict, name='ajax_load_subdistrict'),
    path('hr/ajax/load-uni/', load_union, name='ajax_load_union'),
    path('hr/ajax/load-vil/', load_village, name='ajax_load_village'),
    # path('sign-in/', sign_in, name='signin'),
    # path('logout/', auth_views.logout, {'template_name': 'posts/post_lists.html'}, name='logout'),

]


