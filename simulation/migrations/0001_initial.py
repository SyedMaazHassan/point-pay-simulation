# Generated by Django 3.2.9 on 2022-03-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Simulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('sub_heading', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='simulation')),
            ],
        ),
    ]