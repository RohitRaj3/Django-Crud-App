# Generated by Django 4.2.5 on 2023-09-05 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='lastname',
        ),
    ]
