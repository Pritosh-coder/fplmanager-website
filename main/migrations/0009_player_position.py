# Generated by Django 2.2.5 on 2019-10-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20191013_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(default='', max_length=1),
        ),
    ]
