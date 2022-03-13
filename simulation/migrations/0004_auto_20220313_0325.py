# Generated by Django 3.2.9 on 2022-03-12 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0003_auto_20220313_0015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ('id',)},
        ),
        migrations.RemoveField(
            model_name='step',
            name='video',
        ),
        migrations.AddField(
            model_name='step',
            name='video_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
