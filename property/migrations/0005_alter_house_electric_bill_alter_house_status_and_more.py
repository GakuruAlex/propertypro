# Generated by Django 4.2.11 on 2024-03-25 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('property', '0004_remove_property_no_houses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='electric_bill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property.electricbill'),
        ),
        migrations.AlterField(
            model_name='house',
            name='status',
            field=models.CharField(blank=True, choices=[('AVAILABLE', 'Available'), ('OCCUPIED', 'Occupied')], max_length=20),
        ),
        migrations.AlterField(
            model_name='house',
            name='tenant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.tenant'),
        ),
        migrations.AlterField(
            model_name='house',
            name='water_bill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property.waterbill'),
        ),
    ]