from django import forms
from django.forms import ModelForm
from . import models


class FilmsForm(ModelForm):
    date_sortie = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Films
        fields = ('titre', 'realisateur', 'acteur_principal', 'date_sortie', 'categorie')
        labels = {
            'titre': 'Titre',
            'realisateur': 'Réalisateur',
            'acteur_principal': 'Acteur principal',
            'date_sortie': 'Date de sortie',
            'categorie': 'Genre'
        }


class CatForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = ('titre_cat', 'description')
        labels = {
            'titre_cat': 'Catégorie',
            'description': 'Description',
        }