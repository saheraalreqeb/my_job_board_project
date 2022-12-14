from django.db import models


class Job(models.Model): #job_table
    
    Job_Types = (
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
    )
    
    #this function canges the picture name to a number to make the site faster
    def image_upload(instance, filename):
        image_name , extension = filename.split('.')
        return f'jobs/{instance.id}.{extension}'
    
    title = models.CharField(max_length=100) #our_title_column
    #location
    job_type = models.CharField(max_length=25 , choices=Job_Types , default='') #our_job_type_column
    description = models.TextField(max_length=1000,default='')
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience= models.IntegerField(default=1)
    category= models.ForeignKey('Category',on_delete=models.CASCADE,null=True, blank=True)
    image = models.ImageField(upload_to= image_upload, default='') #will add the jobs folder to the media folder and save it in it
    
    def __str__(self):
        return self.title
    
    
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name