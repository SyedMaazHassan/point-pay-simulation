# Generated by Django 3.2.9 on 2022-03-12 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0005_auto_20220313_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sim-pics'),
        ),
    ]