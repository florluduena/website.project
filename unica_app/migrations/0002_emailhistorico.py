# Generated by Django 3.1.4 on 2020-12-10 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unica_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailHistorico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('request_information', models.TextField(blank=True)),
            ],
        ),
    ]
