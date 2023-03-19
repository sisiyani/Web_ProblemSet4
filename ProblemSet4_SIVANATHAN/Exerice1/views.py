from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from django.http import JsonResponse
import logging

# Create your views here.

contents=[]


class NewContent(forms.Form):
    name = forms.CharField(label='Name',max_length=20)
    newcontent = forms.CharField(label='New content',max_length=150,min_length=10,widget=forms.TextInput(attrs={'id': 'toAdd'}))

class Entry(forms.Form):
    id = forms.IntegerField(label='id', min_value=1, max_value=len(contents))

def homepage(request):
    if request.method == 'POST':
        form = NewContent(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'].title()
            newcontent = form.cleaned_data['newcontent']
            id=len(contents)+1
            data={'id':id,'content':newcontent,'name':name}
            contents.insert(0,{'id':id,'content':newcontent,'name':name})
            return render(request,'Exerice1/homepage.html',{'form': Entry(),'contents':contents[1:],'new':contents[0]})

        else:
            return redirect('add')
    else:
        return render(request,'Exerice1/homepage.html',{'form': Entry(),'contents':contents,'new':None})

def add(request):
    return render(request, 'Exerice1/add.html', {'form': NewContent()})

def entry(request,id):
    if (id<=len(contents)):
        return JsonResponse(contents[id-1])
    else:
        return redirect('')


def entrylevel(request):
    if request.method == 'GET':
        form = Entry(request.GET)
        if form.is_valid():
            id = form.cleaned_data['id']
            return entry(request,id)
        else:
            return redirect('')
    else:
        return redirect('')
