# Generated by Django 3.0.8 on 2020-08-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('img1', models.ImageField(upload_to='')),
                ('img2', models.ImageField(upload_to='')),
                ('content', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Volunteer',
        ),
    ]
