# Generated by Django 5.0.3 on 2024-04-02 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['Stu_name']},
        ),
    ]