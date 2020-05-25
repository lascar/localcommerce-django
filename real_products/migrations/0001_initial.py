# Generated by Django 3.0.6 on 2020-05-25 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('variety', models.CharField(max_length=150)),
                ('aspect', models.CharField(max_length=150)),
                ('packaging', models.CharField(max_length=150)),
                ('size', models.CharField(max_length=150)),
                ('caliber', models.CharField(max_length=150)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'verbose_name': 'Real Product',
                'verbose_name_plural': 'Real Products',
            },
        ),
    ]
