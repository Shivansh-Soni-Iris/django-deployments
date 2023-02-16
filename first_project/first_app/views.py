from django.shortcuts import render
from first_app.models import Accessrecord,Topic,webpage
from first_app import forms
# Create your views here.

from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello World!")
    webpagelist= Accessrecord.objects.order_by('date')
    date_dict={'accRec': webpagelist}
    my_dict = {'insert_me':'Hello i am from views. with first app'}
    return render(request,'first_app/index.html',context=date_dict)

def form_name(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #do something
            print("validation success!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])



    return render(request,'first_app/forms.html',{'forms':form})
#each view will return some httpResponse