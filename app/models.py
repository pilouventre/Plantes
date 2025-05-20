from django.db import models

class Plante(models.Model):
    nom_scientifique = models.CharField(max_length=200)
    nom_commun = models.CharField(max_length=200)
    description = models.TextField()
    famille = models.CharField(max_length=100, blank=True)
    origine = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True) #Type : plante d’intérieur, succulente, grimpante, etc.
    exposition = models.CharField(max_length=100, blank=True) #Lumière : plein soleil, mi-ombre, ombre
    arrosage = models.CharField(max_length=200, blank=True) #Fréquence et conseils d’arrosage
    humidite = models.CharField(max_length=100, blank=True) #Niveau d’humidité recommandé (sec, modéré, humide)
    temperature_min = models.FloatField(null=True, blank=True)
    temperature_max = models.FloatField(null=True, blank=True)
    toxicite = models.BooleanField(default=False)
    floraison = models.CharField(max_length=100, blank=True)
    entretien = models.TextField(blank=True)
    maladies = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_commun or self.nom_scientifique
