# Generated by Django 3.1.4 on 2020-12-11 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unica_app', '0002_emailhistorico'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailhistorico',
            name='emails',
            field=models.TextField(blank=True),
        ),
    ]
