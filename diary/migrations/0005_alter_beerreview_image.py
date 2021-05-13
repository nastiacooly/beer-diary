# Generated by Django 3.2 on 2021-05-13 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_alter_beerreview_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beerreview',
            name='image',
            field=models.URLField(blank=True, default='https://', help_text='Enter URL for beer image', max_length=2000),
        ),
    ]
