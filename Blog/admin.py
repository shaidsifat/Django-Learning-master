from django.contrib import admin
from Blog.models import Blog
from django import forms
# Register your models here.

class ProductForm(forms.ModelForm):
    class Meta:
        model = Blog
        
        fields = ['Name','blog_content']

class BlogAdmin(admin.ModelAdmin):
    #raw_id_fields = ("newspaper",)
    
    fieldsets = (
        ("Personal_Details",{

            "fields":(

                'Name',
                'blog_image',
            ),
        }),
    )
    form = ProductForm
    
    
    

admin.site.register(Blog,BlogAdmin)