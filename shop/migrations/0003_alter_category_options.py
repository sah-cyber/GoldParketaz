# Generated by Django 4.2.5 on 2023-09-18 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_alter_contry_options_shop_categoriya'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoriya', 'verbose_name_plural': 'Categoriya'},
        ),
    ]