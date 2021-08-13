# Generated by Django 3.2.6 on 2021-08-06 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employes', '0003_alter_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]