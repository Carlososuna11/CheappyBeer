# Generated by Django 3.1.1 on 2020-11-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Licores', '0005_licor_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licor',
            name='imagen',
            field=models.ImageField(default='core/Licores/static/Licores/img/Default.jpg', upload_to='core/Licores/static/Licores/img', verbose_name='Imagen del Licor'),
        ),
    ]
