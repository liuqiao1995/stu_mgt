# Generated by Django 2.0 on 2019-06-01 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20, verbose_name='课程名称')),
                ('teacher_name', models.CharField(max_length=20, verbose_name='任课老师')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='MyClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=20, verbose_name='学院')),
                ('grade', models.CharField(choices=[(18, '2018级'), (17, '2017级'), (16, '2016级'), (15, '2015级')], default=16, max_length=20, verbose_name='年级')),
                ('name', models.CharField(choices=[('w1', '物联网工程1班'), ('w2', '物联网工程2班'), ('j1', '计算机1班'), ('j2', '计算机2班'), ('t0', '通信工程卓越班'), ('t1', '通信工程1班'), ('t2', '通信工程2班')], default='w1', max_length=20, verbose_name='班级名称')),
            ],
            options={
                'verbose_name': '班级',
                'verbose_name_plural': '班级',
                'db_table': 'myclass',
            },
        ),
        migrations.CreateModel(
            name='ScoreShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('2016.1', '2016-2017年第一学期'), ('2016.2', '2016-2017年第二学期'), ('2017.1', '2017-2018年第一学期'), ('2017.2', '2017-2018年第二学期'), ('2018.1', '2018-2019年第一学期'), ('2018.2', '2018-2019年第二学期'), ('2019.1', '2019-2020年第一学期'), ('2019.2', '2019-2020年第二学期')], default='2018.2', max_length=20, verbose_name='学期')),
                ('daily_score', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='平时成绩')),
                ('exam_score', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='考试成绩')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acheve_mgt.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '成绩',
                'verbose_name_plural': '成绩',
                'db_table': 'scoreship',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='学号')),
                ('name', models.CharField(max_length=20, verbose_name='学生姓名')),
                ('myclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acheve_mgt.MyClass', verbose_name='班级')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
                'db_table': 'student',
            },
        ),
        migrations.AddField(
            model_name='scoreship',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acheve_mgt.Student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='course',
            name='score',
            field=models.ManyToManyField(related_name='course', through='acheve_mgt.ScoreShip', to='acheve_mgt.Student', verbose_name='学生'),
        ),
    ]