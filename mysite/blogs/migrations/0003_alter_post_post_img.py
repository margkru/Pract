# Generated by Django 3.2.5 on 2021-07-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210715_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
