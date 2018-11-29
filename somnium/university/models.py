from django.db import models

class University(models.Model):
    rectorat = models.CharField(max_length=150)
    kafedra = models.CharField(max_length=150)
    prorector = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    audit = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Rectorat(models.Model):
    name = models.CharField(max_length=50)
    university = models.ManyToManyField(University)

    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
        

class Prorector(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
                