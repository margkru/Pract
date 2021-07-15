# Generated by Django 3.2.5 on 2021-07-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('post_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
