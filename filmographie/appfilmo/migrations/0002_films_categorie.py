# Generated by Django 4.2.2 on 2023-06-12 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appfilmo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='categorie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='appfilmo.categorie'),
        ),
    ]
