# Generated by Django 4.2.2 on 2023-06-15 20:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appfilmo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='acteurs',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='appfilmo.acteurs'),
        ),
        migrations.AlterField(
            model_name='acteurs',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('film', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='appfilmo.films')),
                ('personne', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='appfilmo.personne')),
            ],
        ),
    ]
