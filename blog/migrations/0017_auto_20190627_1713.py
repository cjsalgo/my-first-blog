# Generated by Django 2.0.13 on 2019-06-27 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190627_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='team',
            field=models.ManyToManyField(blank=True, null=True, related_name='posted_to', to='blog.Team'),
        ),
    ]
