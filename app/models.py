from django.db import models

class StudentInfo(models.Model):

    pinno = models.CharField( max_length=13)
    name = models.CharField( max_length=50)
    password = models.CharField(max_length=50,default=" ")
    class Meta:
        verbose_name = ("studentinfo")
        verbose_name_plural = ("studentinfos")

    def __str__(self):
        return self.pinno

    def get_absolute_url(self):
        return reverse("studentinfo_detail", kwargs={"pk": self.pk})

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')

class AdditionalDetails(models.Model):
    def __init__(self, *args):
        super(AdditionalDetails, self).__init__(*args)
    coordinates = models.CharField(max_length=100) 
# Create your models here.
