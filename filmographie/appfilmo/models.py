from django.db import models


class Films(models.Model):
    titre = models.CharField(max_length=100)
    realisateur = models.CharField(max_length=100)
    acteur_principal = models.CharField(max_length=100)
    date_sortie = models.DateField(blank=True, null=True)
    categorie = models.ForeignKey('categorie', on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"{self.titre} réalisé par {self.realisateur} paru le {self.date_sortie}"
        return chaine

    def dico(self):
        return {"titre": self.titre, "realisateur": self.realisateur, "acteur_principal": self.acteur_principal, "date_sortie": self.date_sortie, "categorie": self.categorie}


class Categorie(models.Model):
    titre_cat = models.CharField(max_length=100, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titre_cat

    def dico(self):
        return {"titre_cat": self.titre_cat, "description": self.description}


class Acteurs(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    prenom = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(max_length=3,blank=False)
    films1

    def __str__(self):
        return self.nom

    def dico(self):
        return {"nom": self.nom, "prenom": self.prenom, "age": self.age}