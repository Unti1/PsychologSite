# Generated by Django 4.2.6 on 2023-10-09 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='profession',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='stage',
            field=models.IntegerField(null=True),
        ),
    ]
