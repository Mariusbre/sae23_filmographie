from . import models
from .forms import FilmsForm, CatForm
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
        form = CatForm(request.POST)
        return render(request, "appfilmo/acteurs/formulaire_act.html", {"form": form})
    else:
        form = CatForm()
        return render(request, 'appfilmo/acteurs/formulaire_act.html', {"form": form})


def affichage_act(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/appfilmo/acteurs/index_act/")
    else:
        form = CatForm()
    return render(request, 'appfilmo/acteurs/formulaire_act.html', {"form": form})


def index_act(request):
    liste = list(models.Categorie.objects.all())
    return render(request, 'appfilmo/acteurs/index_act.html', {"liste": liste})


def affiche_acteur(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    return render(request, "appfilmo/acteurs/affiche_acteur.html", {"categorie": categorie})


def update_form_act(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    form = CatForm(instance=categorie)
    return render(request, "appfilmo/acteurs/update_form_cat.html", {"form": form, "id": id})


def update_traitement_act(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    form = CatForm(request.POST, instance=categorie)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/appfilmo/acteurs/index_cat/")
    else:
        return render(request, 'appfilmo/acteurs/update_form_cat.html', {"form": form, "id": id})


def delete_act(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    categorie.delete()
    return HttpResponseRedirect("/appfilmo/acteurs/index_cat/")


def update_act(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    form = CatForm(categorie.dico())
    return render(request, "appfilmo/acteurs/update_form_cat.html", {"form": form, "id": id})
