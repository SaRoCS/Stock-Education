# Generated by Django 3.1.3 on 2021-01-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
