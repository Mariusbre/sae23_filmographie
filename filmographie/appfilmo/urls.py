from django.urls import path
from . import views

urlpatterns = [
    path('films/index/', views.index),
    path('films/affichage/', views.affichage),
    path("", views.index),
    path('films/formulaire/', views.formulaire),
    path('films/affiche_films/<int:id>/', views.affiche_films),
    path('films/update/<int:id>/', views.update),
    path('films/update_traitement/<int:id>/', views.update_traitement),
    path('films/delete/<int:id>/', views.delete),
    path('films/update_form/<int:id>/', views.update_form, name='update_form'),
    path('categorie/affiche_categorie/<int:id>/', views.affiche_categorie),
    path('categorie/formulaire_cat/', views.formulaire_cat),
    path('categorie/update_form_cat/', views.update_form_cat),
    path('categorie/affichage_cat/', views.affichage_cat),
    path('categorie/index_cat/', views.index_cat),
    path('categorie/delete_cat/<int:id>/', views.delete_cat),
    path('categorie/update_cat/<int:id>/', views.update_cat),
    path('categorie/update_traitement_cat/<int:id>/', views.update_traitement_cat),
]