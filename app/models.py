from django.db import models
class Bd(models.Model):
    CIN	=models.CharField(max_length=20)
    Nom=models.CharField(max_length=20)
    Prenom=models.CharField(max_length=20)
    Adresse=models.CharField(max_length=20)
    Email=models.CharField(max_length=80)
    Numerotelephone=models.CharField(max_length=20)
    Profession=models.CharField(max_length=20)
    Departement=models.CharField(max_length=20)

    def __str__(self):
        return self.CIN
    def __str__(self):
        return self.Nom
    def __str__(self):
        return self.Prenom
    def __str__(self):
        return self.Adresse
    def __str__(self):
        return self.Email
    def __str__(self):
        return self.Numerotelephone
    def __str__(self):
        return self.Profession
    def __str__(self):
        return self.Departement

# Create your models here.
