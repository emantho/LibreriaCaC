# Generated by Django 4.2.7 on 2023-12-03 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('editorial', models.CharField(max_length=100)),
                ('precio', models.IntegerField(max_length=10)),
                ('fecha_publicacion', models.DateField(max_length=100)),
                ('isbn', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
