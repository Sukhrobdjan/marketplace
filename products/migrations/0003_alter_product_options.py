# Generated by Django 5.0.4 on 2024-04-26 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-id',)},
        ),
    ]
