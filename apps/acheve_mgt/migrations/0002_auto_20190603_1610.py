# Generated by Django 2.0 on 2019-06-03 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acheve_mgt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreship',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scoreship', to='acheve_mgt.Course', verbose_name='课程'),
        ),
        migrations.AlterField(
            model_name='scoreship',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scoreship', to='acheve_mgt.Student', verbose_name='学生'),
        ),
        migrations.AlterField(
            model_name='student',
            name='myclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='acheve_mgt.MyClass', verbose_name='班级'),
        ),
    ]
