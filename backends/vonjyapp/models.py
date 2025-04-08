from django.db import models

# --------------------------
# Commune
# --------------------------
class Commune(models.Model):
    nomCommune = models.CharField(max_length=30)

    def __str__(self):
        return self.nomCommune

# --------------------------
# Fokotany
# --------------------------
class Fokotany(models.Model):
    nomFokotany = models.CharField(max_length=100)
    classe_responsable = models.CharField(max_length=100)
    nom_responsable = models.CharField(max_length=50)
    prenom_responsable = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    formation_acquise = models.CharField(max_length=10)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name="fokotanys")

    def __str__(self):
        return self.nom

# --------------------------
# Service
# --------------------------
class Service(models.Model):
    nomService = models.CharField(max_length=100)
    description = models.TextField()
    offre = models.TextField()
    membre = models.TextField()
    nombre_membre = models.IntegerField()
    fokotany = models.ForeignKey(Fokotany, on_delete=models.CASCADE, related_name="services")

    def __str__(self):
        return self.nomService

# --------------------------
# Chef de Service
# --------------------------
class ChefService(models.Model):
    nomChef = models.CharField(max_length=50)
    prenomChef = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    adresse = models.TextField()
    sexe = models.CharField(max_length=10)
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name="chef_service")

    def __str__(self):
        return f"{self.nomChef} {self.prenomChef}"

# --------------------------
# Utilisateur
# --------------------------
