# Generated by Django 3.1.7 on 2021-03-16 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
