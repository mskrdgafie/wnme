# Generated by Django 3.0.3 on 2020-11-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yenepay',
            name='buyer_local_id',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]