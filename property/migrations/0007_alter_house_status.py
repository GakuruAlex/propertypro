# Generated by Django 4.2.11 on 2024-03-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_alter_house_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Available'), ('OCCUPIED', 'Occupied')], max_length=20, null=True),
        ),
    ]
