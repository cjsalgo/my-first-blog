# Generated by Django 2.0.13 on 2019-06-22 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
