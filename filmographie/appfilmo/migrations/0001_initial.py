# Generated by Django 4.2.2 on 2023-06-12 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_cat', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('realisateur', models.CharField(max_length=100)),
                ('acteur_principal', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('date_sortie', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
