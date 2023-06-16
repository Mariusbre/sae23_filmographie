from . import models
from .forms import FilmsForm, CatForm, ActForm, PerForm, ComForm
from django.shortcuts import render, HttpResponseRedirect


def accueil(request):
    return render(request, 'appfilmo/accueil.html')


def liste_films(request):
    liste = list(models.Films.objects.all())
    return render(request, 'appfilmo/films/liste_films.html', {"liste": liste})


def formulaire(request):
    if request.method == 'POST':
        form = FilmsForm(request.POST)
        return render(request, "appfilmo/films/formulaire.html", {"form": form})
    else:
        form = FilmsForm()
        return render(request, 'appfilmo/films/formulaire.html', {"form": form})


def affichage(request):
    if request.method == 'POST':
        form = FilmsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/appfilmo/films/liste_films/")
    else:
        form = FilmsForm()
    return render(request, 'appfilmo/films/formulaire.html', {"form": form})


def affiche_films(request, id):
    films = models.Films.objects.get(pk=id)
    liste = list(models.Acteurs.objects.filter(films=films))
    liste3 = list(models.Commentaire.objects.filter(film_id=id))
    liste_note = []
    somme = 0
    max_value = 0
    min_value = 0
    if len(liste3) != 0:
        for commentaire in liste3:
            somme = somme + commentaire.note
            liste_note.append(commentaire.note)
            print('Maximum_value', max_value)
            max_value = max(liste_note)
            print('Minimum_value', min_value)
            min_value = min(liste_note)
        somme = somme / len(liste3)
        print(somme)
        print(max_value)
        print(min_value)

    return render(request, 'appfilmo/films/affiche_films.html', {"films": films, "liste": liste, "liste3": liste3, "somme": somme, 'Maximum_value': max_value, 'Minimum_value': min_value, 'liste_note': liste_note})


def update(request, id):
    films = models.Films.objects.get(pk=id)
    form = FilmsForm(films.dico())
    return render(request, "appfilmo/films/update_form.html", {"form": form, "id": id})


def update_traitement(request, id):
    film = models.Films.objects.get(pk=id)
    form = FilmsForm(request.POST, instance=film)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/appfilmo/films/liste_films/")
    else:
        return render(request, 'appfilmo/films/update_form.html', {"form": form, "id": id})


def delete(request, id):
    films = models.Films.objects.get(pk=id)
    films.delete()
    return HttpResponseRedirect("/appfilmo/films/liste_films/")


def update_form(request, id):
    films = models.Films.objects.get(pk=id)
    form = FilmsForm(instance=films)
    return render(request, "appfilmo/films/update_form.html", {"form": form, "id": id})


####


def formulaire_cat(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        return render(request, "appfilmo/categorie/formulaire_cat.html", {"form": form})
    else:
        form = CatForm()
        return render(request, 'appfilmo/categorie/formulaire_cat.html', {"form": form})


def affichage_cat(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/appfilmo/categorie/liste_cat/")
    else:
        form = CatForm()
    return render(request, 'appfilmo/categorie/formulaire_cat.html', {"form": form})


def liste_cat(request):
    liste = list(models.Categorie.objects.all())
    return render(request, 'appfilmo/categorie/liste_cat.html', {"liste": liste})


def affiche_categorie(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    return render(request, "appfilmo/categorie/affiche_categorie.html", {"categorie": categorie})


def update_form_cat(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    form = CatForm(instance=categorie)
    return render(request, "appfilmo/categorie/update_form_cat.html", {"form": form, "id": id})


def update_traitement_cat(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    form = CatForm(request.POST, instance=categorie)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/appfilmo/categorie/liste_cat/")
    else:
        return render(request, 'appfilmo/categorie/update_form_cat.html', {"form": form, "id": id})


def delete_cat(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    categorie.delete()
    return HttpResponseRedirect("/appfilmo/categorie/liste_cat/")


def update_cat(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    form = CatForm(categorie.dico())
    return render(request, "appfilmo/categorie/update_form_cat.html", {"form": form, "id": id})

##


def formulaire_act(request):
    if request.method == 'POST':
        form = ActForm(request.POST)
        return render(request, "appfilmo/acteurs/formulaire_act.html", {"form": form})
    else:
        form = ActForm()
        return render(request, 'appfilmo/acteurs/formulaire_act.html', {"form": form})


def affichage_act(request):
    if request.method == 'POST':
        form = ActForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/appfilmo/acteurs/liste_act/")
    else:
        form = ActForm()
    return render(request, 'appfilmo/acteurs/formulaire_act.html', {"form": form})


def liste_act(request):
    liste = list(models.Acteurs.objects.all())
    return render(request, 'appfilmo/acteurs/liste_act.html', {"liste": liste})


def affiche_acteur(request, id):
    acteurs = models.Acteurs.objects.get(pk=id)
    return render(request, "appfilmo/acteurs/affiche_acteur.html", {"acteurs": acteurs})


def update_form_act(request, id):
    acteurs = models.Acteurs.objects.get(pk=id)
    form = ActForm(instance=acteurs)
    return render(request, "appfilmo/acteurs/update_form_act.html", {"form": form, "id": id})


def update_traitement_act(request, id):
    acteurs = models.Acteurs.objects.get(pk=id)
    form = ActForm(request.POST, instance=acteurs)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/appfilmo/acteurs/liste_act/")
    else:
        return render(request, 'appfilmo/acteurs/update_form_act.html', {"form": form, "id": id})


def delete_act(request, id):
    acteurs = models.Acteurs.objects.get(pk=id)
    acteurs.delete()
    return HttpResponseRedirect("/appfilmo/acteurs/liste_act/")


def update_act(request, id):
    acteurs = models.Acteurs.objects.get(pk=id)
    form = ActForm(acteurs.dico())
    return render(request, "appfilmo/acteurs/update_form_act.html", {"form": form, "id": id})


####


def formulaire_per(request):
    if request.method == 'POST':
        form = PerForm(request.POST)
        return render(request, "appfilmo/personne/formulaire_per.html", {"form": form})
    else:
        form = PerForm()
        return render(request, 'appfilmo/personne/formulaire_per.html', {"form": form})


def affichage_per(request):
    if request.method == 'POST':
        form = PerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/appfilmo/personne/liste_per/")
    else:
        form = PerForm()
    return render(request, 'appfilmo/personne/formulaire_per.html', {"form": form})


def liste_per(request):
    liste = list(models.Personne.objects.all())
    return render(request, 'appfilmo/personne/liste_per.html', {"liste": liste})


def affiche_personne(request, id):
    personne = models.Personne.objects.get(pk=id)
    return render(request, "appfilmo/personne/affiche_personne.html", {"personne": personne})


def update_form_per(request, id):
    personne = models.Personne.objects.get(pk=id)
    form = PerForm(instance=personne)
    return render(request, "appfilmo/personne/update_form_per.html", {"form": form, "id": id})


def update_traitement_per(request, id):
    personne = models.Personne.objects.get(pk=id)
    form = PerForm(request.POST, instance=personne)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/appfilmo/personne/liste_per/")
    else:
        return render(request, 'appfilmo/personne/update_form_per.html', {"form": form, "id": id})


def delete_per(request, id):
    personne = models.Personne.objects.get(pk=id)
    personne.delete()
    return HttpResponseRedirect("/appfilmo/personne/liste_per/")


def update_per(request, id):
    personne = models.Personne.objects.get(pk=id)
    form = PerForm(personne.dico())
    return render(request, "appfilmo/personne/update_form_per.html", {"form": form, "id": id})

##


def liste_com(request):
    liste = list(models.Commentaire.objects.all())
    return render(request, 'appfilmo/commentaire/liste_com.html', {"liste": liste})


def formulaire_com(request):
    if request.method == 'POST':
        form = ComForm(request.POST)
        return render(request, "appfilmo/commentaire/formulaire_com.html", {"form": form})
    else:
        form = ComForm()
        return render(request, 'appfilmo/commentaire/formulaire_com.html', {"form": form})


def affichage_com(request):
    if request.method == 'POST':
        form = ComForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/appfilmo/commentaire/liste_com/")
    else:
        form = ComForm()
    return render(request, 'appfilmo/commentaire/formulaire_com.html', {"form": form})


def affiche_commentaire(request, id):
    commentaire = models.Commentaire.objects.get(pk=id)
    return render(request, "appfilmo/commentaire/affiche_commentaire.html", {"commentaire": commentaire})


def update_com(request, id):
    com = models.Commentaire.objects.get(pk=id)
    form = ComForm(com.dico())
    return render(request, "appfilmo/commentaire/update_form_com.html", {"form": form, "id": id})


def update_traitement_com(request, id):
    film = models.Commentaire.objects.get(pk=id)
    form = ComForm(request.POST, instance=film)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/appfilmo/commentaire/liste_com/")
    else:
        return render(request, 'appfilmo/commentaire/update_form_com.html', {"form": form, "id": id})


def delete_com(request, id):
    films = models.Commentaire.objects.get(pk=id)
    films.delete()
    return HttpResponseRedirect("/appfilmo/commentaire/liste_com/")


def update_form_com(request, id):
    films = models.Commentaire.objects.get(pk=id)
    form = ComForm(instance=films)
    return render(request, "appfilmo/commentaire/update_form_com.html", {"form": form, "id": id})
