from django.db import models
from django.core.exceptions import ValidationError



# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.IntegerField()
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Signup(models.Model):
    name = models.CharField(max_length=122)
    surname = models.CharField(max_length=122)
    phone = models.IntegerField()
    email = models.CharField(max_length=122)
    add = models.CharField(max_length=122)
    file = models.ImageField(upload_to='media', blank=True)
    pwd= models.CharField(max_length=122)
    rpwd= models.CharField(max_length=122)

    def __str__(self):
         return self.name + ": " + str(self.file)

class Login(models.Model):
    uname = models.CharField(max_length=122)
    psw= models.CharField(max_length=122)

    def __str__(self):
        return self.uname

class Complaint(models.Model):
    name = models.CharField(max_length=122)
    # BullyingType = models.BooleanField(default=False)
    # ResultInInjury = models.BooleanField(default=False)
    # BullyBehaviors = models.BooleanField(default=False)
    place = models.CharField(max_length=122)
    Description= models.CharField(max_length=122)
    PhysicalEvidence= models.CharField(max_length=122)
    fileUpload = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.name + ": " + str(self.fileUpload)


    

    