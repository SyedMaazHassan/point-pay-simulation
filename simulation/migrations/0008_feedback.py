# Generated by Django 3.2.9 on 2022-03-13 12:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0007_alter_step_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
