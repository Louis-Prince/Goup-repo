from django.shortcuts import redirect, render,HttpResponse
from .forms import conferenceforms
from .models import conference
from .models import Speaker_management
from .forms import Speaker_form
from .forms import Scheduleform
# Create your views here.
def index(request):
   context={
      'conferences': conference.objects.all()
   }
   return render(request,'index.html' , context)


def conferenceregister(request):
   form=conferenceforms()
   if request.method=='POST':
      form=conferenceforms(request.POST)
      if form.is_valid():
         form.save()
         return redirect('index')
   else:
    print(form.errors)
   return render(request, 'conference.html', {'form':form}) 


def conferencedetails(request, id):
   context={}
   context['detail']=conference.objects.get(id=id)
   return render(request, 'conferencedetail.html', context)

def speaker_forms(request):
        form = Speaker_form(request.POST or None)
        if form.is_valid():
            form.save()
            form=Speaker_form() 
        context = {
            'form': form
              
        }   
        return render (request, 'speaker_form.html',{'form':form})
     
def schedule_forms(request):
   form =Scheduleform(request.POST or None)
   if form.is_valid():
            form.save()
            form=Speaker_form() 
   context = {
            'form': form
              
        }   
   return render (request, 'sheduleform.html',{'form':form})
def speaker_list(request):
    speakers = Speaker_management.objects.all()
    return render(request, 'allspeakers.html', {'speakers': speakers})
 
def details_of_speaker(request, id):
    myevent = Speaker_management.objects.get(id=id)
    template = loader.get_template('speaker_details.html')
    context = {
          'mymember': myevent,
           }
    return HttpResponse(template.render(context,request))