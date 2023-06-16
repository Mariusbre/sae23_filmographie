from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Films(models.Model):
    titre = models.CharField(max_length=100)
    realisateur = models.CharField(max_length=100)
    date_sortie = models.DateField(blank=True, null=True)
    categorie = models.ForeignKey('categorie', on_delete=models.CASCADE, default=None)
    acteurs = models.ForeignKey('acteurs', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.titre

    def dico(self):
        return {"titre": self.titre, "realisateur": self.realisateur, "date_sortie": self.date_sortie,
                "categorie": self.categorie, "acteurs": self.acteurs}


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
    age = models.IntegerField(validators=[MinValueValidator(0)],blank=False)

    def __str__(self):
        return self.nom

    def dico(self):
        return {"nom": self.nom, "prenom": self.prenom, "age": self.age}


class Personne(models.Model):
    pro = 'PROFESSIONEL'
    ama = 'AMATEUR'
    type = [
        (pro, 'PROFESSIONEL'),
        (ama, 'AMATEUR'),
    ]
    pseudo = models.CharField(max_length=100, blank=False)
    nomprenom = models.CharField(max_length=100, blank=False)
    mail = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    type = models.CharField(max_length=30, choices=type, default=ama, blank=False)

    def __str__(self):
        return self.pseudo

    def dico(self):
        return {"pseudo": self.pseudo, "nomprenom": self.nomprenom, "mail": self.mail, "type": self.type,
                "password": self.password}


class Commentaire(models.Model):
    film = models.ForeignKey('films', on_delete=models.CASCADE, default=None)
    personne = models.ForeignKey('personne', on_delete=models.CASCADE, default=None)
    note = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    commentaire = models.TextField(null=True, blank=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        chaine = f" {self.personne} a commenté {self.film}"
        return chaine

    def dico(self):
        return {"film": self.film, "personne": self.personne, "note": self.note, "commentaire": self.commentaire,
                "date": self.date}
