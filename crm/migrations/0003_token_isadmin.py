# Generated by Django 2.2.4 on 2019-08-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20190817_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='isAdmin',
            field=models.BooleanField(default=False),
        ),
    ]
