# Generated by Django 4.0.3 on 2022-05-26 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_rating_andcomments_using_exp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='comments_count',
            field=models.IntegerField(default=0, verbose_name='Кол-во отзывов'),
        ),
        migrations.AddField(
            model_name='tovar',
            name='recommendation',
            field=models.SmallIntegerField(null=True, verbose_name='Процент рекомендаций'),
        ),
        migrations.AlterField(
            model_name='tovar',
            name='rating',
            field=models.FloatField(default=0, verbose_name='Рейтинг'),
        ),
    ]
