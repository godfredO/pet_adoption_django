from django.db import models

# Create your models here.
class Pet(models.Model):
    sex_choices = [('M','Male'), ('F','Female')]
    name = models.CharField(max_length=100) #max_length is a required keyword argument for CharField
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    submission_date = models.DateTimeField()
    description = models.TextField(blank=True)
    sex = models.CharField(max_length=1, choices=sex_choices, blank = True) #blank=True means this field is not required and can be left empty
    age = models.IntegerField(null=True) #null=True means an empty value is stored as Null, not zero
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
 