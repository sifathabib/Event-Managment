# Generated by Django 5.1.6 on 2025-02-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
