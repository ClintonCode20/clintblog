# Generated by Django 3.1 on 2021-07-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='image/fs1.jpg', upload_to=''),
        ),
    ]
