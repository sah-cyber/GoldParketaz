# Generated by Django 4.2.5 on 2023-09-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250, verbose_name='Bashliq')),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('text', models.TextField(verbose_name='Etrafli')),
                ('carusel_img', models.ImageField(upload_to='Carusel_img/%Y/%m/%d/', verbose_name='Carusel_sekil')),
                ('creted_at', models.DateTimeField(auto_now_add=True, verbose_name='Qeyd_tarixi')),
                ('creted_up', models.DateTimeField(auto_now=True, verbose_name='Yenilenme_tarixi')),
                ('public', models.BooleanField(default=True, verbose_name='Derc_edilib')),
            ],
            options={
                'verbose_name': 'Carusel',
                'verbose_name_plural': 'Carusel',
            },
        ),
    ]
