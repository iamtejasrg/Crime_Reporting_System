# Generated by Django 3.2.3 on 2021-06-15 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=122)),
                ('psw', models.CharField(max_length=122)),
            ],
        ),
    ]
