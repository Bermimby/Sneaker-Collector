# Generated by Django 4.1.6 on 2023-02-11 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('Sneaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.sneaker')),
            ],
        ),
    ]
