from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.accueil),
    ##
    path('films/liste_films/', views.liste_films),
    path('films/affichage/', views.affichage),
    path("", views.accueil),
    path('films/formulaire/', views.formulaire),
    path('films/affiche_films/<int:id>/', views.affiche_films),
    path('films/update/<int:id>/', views.update),
    path('films/update_traitement/<int:id>/', views.update_traitement),
    path('films/delete/<int:id>/', views.delete),
    path('films/update_form/<int:id>/', views.update_form, name='update_form'),
    ##
    path('categorie/affiche_categorie/<int:id>/', views.affiche_categorie),
    path('categorie/formulaire_cat/', views.formulaire_cat),
    path('categorie/update_form_cat/', views.update_form_cat),
    path('categorie/affichage_cat/', views.affichage_cat),
    path('categorie/liste_cat/', views.liste_cat),
    path('categorie/delete_cat/<int:id>/', views.delete_cat),
    path('categorie/update_cat/<int:id>/', views.update_cat),
    path('categorie/update_traitement_cat/<int:id>/', views.update_traitement_cat),
    ##
    path('acteurs/affiche_acteur/<int:id>/', views.affiche_acteur),
    path('acteurs/formulaire_act/', views.formulaire_act),
    path('acteurs/update_form_act/', views.update_form_act),
    path('acteurs/affichage_act/', views.affichage_act),
    path('acteurs/liste_act/', views.liste_act),
    path('acteurs/delete_act/<int:id>/', views.delete_act),
    path('acteurs/update_act/<int:id>/', views.update_act),
    path('acteurs/update_traitement_act/<int:id>/', views.update_traitement_act),
    ##
    path('personne/affiche_personne/<int:id>/', views.affiche_personne),
    path('personne/formulaire_per/', views.formulaire_per),
    path('personne/update_form_per/', views.update_form_per),
    path('personne/affichage_per/', views.affichage_per),
    path('personne/liste_per/', views.liste_per),
    path('personne/delete_per/<int:id>/', views.delete_per),
    path('personne/update_per/<int:id>/', views.update_per),
    path('personne/update_traitement_per/<int:id>/', views.update_traitement_per),
    ##
    path('commentaire/affiche_commentaire/<int:id>/', views.affiche_commentaire),
    path('commentaire/formulaire_com/', views.formulaire_com),
    path('commentaire/update_form_com/', views.update_form_com),
    path('commentaire/affichage_com/', views.affichage_com),
    path('commentaire/liste_com/', views.liste_com),
    path('commentaire/delete_com/<int:id>/', views.delete_com),
    path('commentaire/update_com/<int:id>/', views.update_com),
    path('commentaire/update_traitement_com/<int:id>/', views.update_traitement_com),
]