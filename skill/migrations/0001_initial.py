# Generated by Django 3.2.5 on 2022-08-06 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myskill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='skillimage/')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField(blank=True, max_length=500)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
