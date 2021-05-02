# Generated by Django 3.2 on 2021-05-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beertype',
            name='filtered',
            field=models.CharField(blank=True, choices=[('y', 'filtered'), ('n', 'unfiltered')], help_text='Choose filtered or unfiltered', max_length=1, null=True),
        ),
    ]
