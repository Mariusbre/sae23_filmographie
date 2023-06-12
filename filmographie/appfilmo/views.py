from . import models
from .forms import FilmsForm, CatForm, ActForm, PerForm, LienForm
from django.shortcuts import render, HttpResponseRedirect


def index_main(request):
    return render(request, 'appfilmo/index_main.html')


def index(request):
    liste = list(models.Films.objects.all())
    return render(request, 'appfilmo/films/index.html', {"liste": liste})


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
            return HttpResponseRedirect("/appfilmo/films/index/")
    else:
        form = FilmsForm()
    return render(request, 'appfilmo/films/formulaire.html', {"form": form})


def affiche_films(request, id):
    films = models.Films.objects.get(pk=id)
    return render(request, "appfilmo/films/affiche_films.html", {"films": films})


def update(request, id):
    films = models.Films.objects.get(pk=id)
    form = FilmsForm(films.dico())
    return render(request, "appfilmo/films/update_form.html", {"form": form, "id": id})


def update_traitement(request, id):
    film = models.Films.objects.get(pk=id)
    form = FilmsForm(request.POST, instance=film)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/appfilmo/films/index/")
    else:
        return render(request, 'appfilmo/films/update_form.html', {"form": form, "id": id})


def delete(request, id):
    films = models.Films.objects.get(pk=id)
    films.delete()
    return HttpResponseRedirect("/appfilmo/films/index/")


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
            return HttpResponseRedirect("/appfilmo/categorie/index_cat/")
    else:
        form = CatForm()
    return render(request, 'appfilmo/categorie/formulaire_cat.html', {"form": form})


def index_cat(request):
    liste = list(models.Categorie.objects.all())
    return render(request, 'appfilmo/categorie/index_cat.html', {"liste": liste})


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
        return HttpResponseRedirect("/appfilmo/categorie/index_cat/")
    else:
        return render(request, 'appfilmo/categorie/update_form_cat.html', {"form": form, "id": id})


def delete_cat(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    categorie.delete()
    return HttpResponseRedirect("/appfilmo/categorie/index_cat/")


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
            return HttpResponseRedirect("/appfilmo/acteurs/index_act/")
    else:
        form = ActForm()
    return render(request, 'appfilmo/acteurs/formulaire_act.html', {"form": form})


def index_act(request):
    liste = list(models.Acteurs.objects.all())
    return render(request, 'appfilmo/acteurs/index_act.html', {"liste": liste})


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
        return HttpResponseRedirect("/appfilmo/acteurs/index_act/")
    else:
        return render(request, 'appfilmo/acteurs/update_form_act.html', {"form": form, "id": id})


def delete_act(request, id):
    acteurs = models.Acteurs.objects.get(pk=id)
    acteurs.delete()
    return HttpResponseRedirect("/appfilmo/acteurs/index_act/")


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
            return HttpResponseRedirect("/appfilmo/personne/index_per/")
    else:
        form = PerForm()
    return render(request, 'appfilmo/personne/formulaire_per.html', {"form": form})


def index_per(request):
    liste = list(models.Personne.objects.all())
    return render(request, 'appfilmo/personne/index_per.html', {"liste": liste})


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
        return HttpResponseRedirect("/appfilmo/personne/index_per/")
    else:
        return render(request, 'appfilmo/personne/update_form_per.html', {"form": form, "id": id})


def delete_per(request, id):
    personne = models.Personne.objects.get(pk=id)
    personne.delete()
    return HttpResponseRedirect("/appfilmo/personne/index_per/")


def update_per(request, id):
    personne = models.Personne.objects.get(pk=id)
    form = PerForm(personne.dico())
    return render(request, "appfilmo/personne/update_form_per.html", {"form": form, "id": id})
