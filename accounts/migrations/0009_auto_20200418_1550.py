# Generated by Django 3.0.4 on 2020-04-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200418_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
