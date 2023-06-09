# Generated by Django 4.1.4 on 2022-12-28 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('less_app', '0004_course_student_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='schools',
            field=models.ManyToManyField(to='less_app.school'),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
