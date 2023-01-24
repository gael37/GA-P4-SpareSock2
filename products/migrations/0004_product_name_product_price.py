# Generated by Django 4.1.4 on 2022-12-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
