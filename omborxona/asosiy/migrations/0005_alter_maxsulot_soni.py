# Generated by Django 4.2.3 on 2023-08-08 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0004_alter_maxsulot_ombor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maxsulot',
            name='soni',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
