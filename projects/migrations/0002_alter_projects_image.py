# Generated by Django 4.0.3 on 2022-04-10 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(default='https://wallpaperaccess.com/full/1129018.jpg', upload_to='projects/'),
        ),
    ]
