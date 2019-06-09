# Generated by Django 2.2.2 on 2019-06-08 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(max_length=200)),
                ('price', models.PositiveIntegerField(default=0)),
                ('featured', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
