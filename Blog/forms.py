from django import forms
from django.contrib import admin
from myapp.models import Blog

class PersonForm(forms.ModelForm):

    class Meta:
        model = Blog
        include = ['visible']
       
        fields = ['Name','blog_content']


class PersonAdmin(admin.ModelAdmin):
    exclude = ['button']
    form = PersonForm