# Generated by Django 2.0 on 2019-06-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acheve_mgt', '0005_auto_20190603_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myclass',
            name='dept',
            field=models.CharField(choices=[('信息', '信息工程学院')], default='信息', max_length=20, verbose_name='学院'),
        ),
        migrations.AlterField(
            model_name='myclass',
            name='name',
            field=models.CharField(choices=[('w1', '物联网工程1班'), ('w2', '物联网工程2班'), ('j1', '计算机1班'), ('j2', '计算机2班'), ('t0', '通信工程卓越班'), ('t1', '通信工程1班'), ('t2', '通信工程2班')], default='w1', max_length=20, verbose_name='班级名称'),
        ),
        migrations.AlterUniqueTogether(
            name='myclass',
            unique_together={('grade', 'name')},
        ),
    ]
