# Generated by Django 3.0.4 on 2020-04-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200418_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='aboutMe',
            field=models.CharField(blank=True, default='Su di me..', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, default='Numero di telefono', max_length=50, null=True),
        ),
    ]
