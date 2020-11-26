# Generated by Django 3.1.1 on 2020-11-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Licores', '0007_auto_20201124_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licor',
            name='ubicacion',
            field=models.TextField(choices=[('Santa Rosalía', 'Santa Rosalía'), ('El Valle', 'El Valle'), ('Coche', 'Coche'), ('Caricuao', 'Caricuao'), ('Macarao', 'Macarao'), ('Antimano', 'Antímano'), ('La Vega', 'La Vega'), ('El Paraíso', 'El Paraíso'), ('El Junquito', 'El Junquito'), ('Sucre (Catia)', 'Sucre (Catia)'), ('San Juan', 'San Juan'), ('Santa Teresa', 'Santa Teresa'), ('23 de enero', '23 de enero'), ('La Pastora', 'La Pastora'), ('Altagracia', 'Altagracia'), ('San José', 'San José'), ('San Bernardino', 'San Bernardino'), ('Catedral', 'Catedral'), ('Candelaria', 'Candelaria'), ('San Agustín', 'San Agustín'), ('El Recreo', 'El Recreo'), ('San Pedro', 'San Pedro')], default='El Recreo', verbose_name='Ubicación'),
        ),
    ]
