# Generated by Django 5.1.2 on 2024-11-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buses',
            name='passenger',
        ),
        migrations.AddField(
            model_name='buses',
            name='passenger',
            field=models.ManyToManyField(related_name='onboard', to='buses.passenger'),
        ),
    ]
