from django.db import models

class StudentInfo(models.Model):

    pinno = models.CharField( max_length=13)
    name = models.CharField( max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
        verbose_name = ("studentinfo")
        verbose_name_plural = ("studentinfos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("studentinfo_detail", kwargs={"pk": self.pk})

# Create your models here.
