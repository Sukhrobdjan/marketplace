# Generated by Django 5.0.4 on 2024-05-04 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video_file',
            field=models.FileField(default=1, upload_to='videos/'),
            preserve_default=False,
        ),
    ]