# Generated by Django 2.2.3 on 2019-10-18 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='source',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]