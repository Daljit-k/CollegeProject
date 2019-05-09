from django.db import models

class signup(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    image = models.FileField()
    #image = models.FileField(upload_to='images/')
    def __str__(self):
                return self.firstname + '==>' + self.lastname+ '==>' + self.email + '==>' + self.password + '==>' + self.gender
class contactform(models.Model):
    uid = models.CharField(max_length=40)
    uname = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    message = models.CharField(max_length=40)



import datetime
class complaint(models.Model):
    #date = models.DateField(_("Date"), default=datetime.date.today)
    date = models.DateField(default=datetime.date.today)
    uid=models.CharField(max_length=40)
    #date= models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    mobile=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    subaddress = models.CharField(max_length=40)
    complaint_detail = models.CharField(max_length=40)
    status1 = models.CharField(max_length=40)
    def __str__(self):
                return self.uid + '==>' + self.username+ '==>' + self.email + '==>' + self.complaint_detail

