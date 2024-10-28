# Generated by Django 5.0.4 on 2024-09-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_personinfor'),
    ]

    operations = [
        migrations.AddField(
            model_name='personinfor',
            name='stats',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personinfor',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personinfor',
            name='first_name',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personinfor',
            name='second_name',
            field=models.CharField(blank=True, null=True),
        ),
    ]