# Generated by Django 3.1 on 2020-09-15 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='midify_date',
            new_name='modify_date',
        ),
    ]
