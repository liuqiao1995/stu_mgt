# Generated by Django 2.0 on 2019-06-02 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=40, verbose_name='密码'),
        ),
    ]
