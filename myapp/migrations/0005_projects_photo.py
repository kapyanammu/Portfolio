# Generated by Django 4.2.1 on 2023-05-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_link_projects_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='photo',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
