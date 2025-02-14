# Generated by Django 5.0.7 on 2024-07-14 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=250)),
                ('image', models.ImageField(upload_to='course/speciality/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.FloatField(default=0)),
                ('rating', models.FloatField(default=0)),
                ('active_students', models.PositiveIntegerField(default=0)),
                ('speciality', models.ManyToManyField(to='course.speciality')),
            ],
        ),
    ]
