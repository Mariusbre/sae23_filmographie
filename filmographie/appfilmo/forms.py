from django import forms
from django.forms import ModelForm
from . import models


class FilmsForm(ModelForm):
    date_sortie = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Films
        fields = ('titre', 'realisateur', 'date_sortie', 'categorie', 'acteurs')
        labels = {
            'titre': 'Titre',
            'realisateur': 'Réalisateur',
            'date_sortie': 'Date de sortie',
            'categorie': 'Genre',
            'acteurs': 'Acteurs',
        }


class CatForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = ('titre_cat', 'description')
        labels = {
            'titre_cat': 'Catégorie',
            'description': 'Description',
        }


class ActForm(ModelForm):
    class Meta:
        model = models.Acteurs
        fields = ('nom', 'prenom', 'age')
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'age': 'Age',
        }


class PerForm(ModelForm):
    class Meta:
        model = models.Personne
        fields = ('pseudo', 'nomprenom', 'mail', 'password', 'type')
        labels = {
            'pseudo': 'Pseudo',
            'nomprenom': 'Nom et prénom',
            'mail': 'Mail',
            'password': 'Mot de passe',
            'type': 'Type',
        }


class ComForm(ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Commentaire
        fields = ('film', 'personne', 'note', 'commentaire', 'date')
        labels = {
            'film': 'Film',
            'personne': 'Personne',
            'note': 'Note',
            'commentaire': 'Commentaire',
            'date': 'date',
        }