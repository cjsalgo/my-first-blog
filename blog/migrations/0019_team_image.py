# Generated by Django 2.0.13 on 2019-06-28 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_remove_team_sent_applications'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, upload_to='team_images'),
        ),
    ]