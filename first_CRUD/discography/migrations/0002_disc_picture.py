# Generated by Django 4.2.13 on 2024-06-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discography', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disc',
            name='Picture',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]