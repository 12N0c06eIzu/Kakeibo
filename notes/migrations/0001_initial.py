# Generated by Django 4.1.3 on 2023-01-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kakeibo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='タイトル')),
                ('money', models.IntegerField(max_length=128, verbose_name='金額')),
                ('tag', models.CharField(blank=True, max_length=30, verbose_name='タグ')),
                ('trading_dt', models.DateTimeField(verbose_name='取引日')),
                ('io_flag', models.CharField(max_length=30, verbose_name='入出フラグ')),
                ('created_dt', models.DateTimeField(auto_now=True, verbose_name='作成日')),
                ('updated_dt', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
    ]
