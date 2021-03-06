# Generated by Django 4.0.3 on 2022-05-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_rating_andcomments_tovar_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating_andcomments',
            name='comment',
            field=models.TextField(null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='rating_andcomments',
            name='rating',
            field=models.FloatField(default=0, verbose_name='Рейтинг'),
        ),
    ]
