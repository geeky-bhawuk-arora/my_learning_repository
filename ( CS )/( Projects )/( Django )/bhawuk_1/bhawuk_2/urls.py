from django.urls import path
from bhawuk_2 import views


urlpatterns = [

   path('',views.home, name='go_to_home'),
   path('home/',views.home, name='go_to_home'),
   path('about/',views.about, name='go_to_about'),
   path('ro_creation',views.ro_creation, name='go_to_ro_creation'),
   path('support/',views.support, name='go_to_support')
   
   ]
    

