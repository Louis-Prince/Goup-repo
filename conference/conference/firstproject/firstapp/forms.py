from django import forms
from firstapp.models import conference
from firstapp.models import Speaker_management
from firstapp.models import Schedule_management
class conferenceforms(forms.ModelForm):
    class Meta:
        model= conference
        fields='__all__'
        
class Speaker_form(forms.ModelForm):
    class Meta:
        model = Speaker_management
        fields = ['name', 'biography', 'photo', 'email', 'phone_number', 'linkedin_link', 'twitter_link']

class Scheduleform(forms.ModelForm):
    class Meta:
          model = Schedule_management
          fields = ['start_time','end_time','topic','speaker']
            