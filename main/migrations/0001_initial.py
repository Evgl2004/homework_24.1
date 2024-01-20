# Generated by Django 5.0.1 on 2024-01-20 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='course/', verbose_name='картинка (превью)')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='course/', verbose_name='картинка (превью)')),
                ('description', models.TextField(verbose_name='описание')),
                ('link_to_video', models.CharField(blank=True, max_length=250, null=True, verbose_name='ссылка на видео')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]
