from datetime import date
from django.db import models
from django.db.models.fields import CharField
from django.db.models.query_utils import select_related_descend
from matplotlib.pyplot import cla
from numpy import mod
from pandas.core.algorithms import mode




class Contect(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=50)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self) :
        return self.name


class Customer(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=50)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self) :
        return self.name


class Strokes(models.Model):
    stroke_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=2000)
    swimmer=models.CharField(max_length=2000)
    tags=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images")
    event=models.FileField(upload_to='images')

    
    def __str__(self) :
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(('Indoor','Indoor'),('OUTDOOR','OUTDOOR'),)

    name=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=200,null=True)
    date_crerated=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS=(('pending','pending'),('out for delivery','out for delivery'),('deliverd','deliverd'))

    customer=models.ForeignKey(Customer,null=True,on_delete=Customer)
    product=models.ForeignKey(Product,null=True,on_delete=Product)

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()

    author=models.CharField(max_length=13)
    timeStamp=models.DateTimeField(blank=True)
    slug=models.CharField(max_length=130)
    

    def __str__(self):
        return self.title + 'by' + self.author




class Swimmers_pool(models.Model):
    swimmer_id=models.AutoField(primary_key=True)
    Swiimmingpool_name=models.CharField(max_length=2000)
   
    swimmer_tags=models.CharField(max_length=100)
    swimmer_image=models.ImageField(upload_to="images")
    swimmer_event=models.FileField(upload_to='images')
    
    

    
    def __str__(self) :
        return self.Swiimmingpool_name


class My_swimming_students(models.Model):
    student_id=models.AutoField(primary_key=True)
    student_name=models.CharField(max_length=200)
    student_interest=models.TextField()

    student_favourite_stroke=models.CharField(max_length=13)
    
    slug=models.CharField(max_length=130)
    def __str__(self) :
        return self.student_name


# Create your models here.

class Chartapp(models.Model):
     name=models.CharField(max_length=122)
     email=models.CharField(max_length=122)
     phone=models.CharField(max_length=50)
     desc=models.TextField()
     date=models.DateField()


     def __str__(self):
         return f'{self.name} - {self.date}'
         
class Age(models.Model):
    
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=50)
    how_old=models.PositiveIntegerField()


    def __str__(self):
        return self.name
     
class Matplotlib(models.Model):

    item_name=models.CharField(max_length=122)
    price=models.PositiveIntegerField()

    def __str__(self):
        return f'{self.item_name} - {self.price}'
    
class Compititions(models.Model):

    comp_name=models.CharField(max_length=200)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.comp_name
    

class Participants(models.Model):
    #comp=models.ForeignKey(Compititions,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    comp1=models.ManyToManyField(Compititions)

    def __str__(self):
        return f'{self.comp1} - {self.name}'


class Sports(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name
    


class Style(models.Model):
    name=models.CharField(max_length=10)
    sports_name=models.ForeignKey(Sports,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Topic(models.Model):
    top_name=models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=264,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return str(self.date)
    


    
    

