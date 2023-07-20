from django.urls import path, include
from . import views
urlpatterns = [
   path("",views.index, name="index"),
   path('registerconference', views.conferenceregister, name='registerconference'),
   path('conferencedetail/<int:id>/', views.conferencedetails, name='conferencedetail'),
   path('speaker/forms',views.speaker_forms),
   path('schedule/forms',views.schedule_forms),
   path('all/speakers',views.speaker_list),
   path('speaker/list/details/<int:id>', views.details_of_speaker),
   
]