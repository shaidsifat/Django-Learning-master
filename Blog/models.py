from django.db import models

# Create your models here.
class Blog(models.Model):
    
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=220)
    blog_image = models.ImageField(upload_to='media/blog',null=True,blank=True)
    blog_content = models.TextField(max_length=2200)
    
    def __str__(self):

        return self.Name


