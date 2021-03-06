# Generated by Django 4.0.2 on 2022-02-14 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationships', '0004_relationship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(default='beginer', max_length=50)),
                ('course_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relationships.course')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationships.student')),
            ],
        ),
        migrations.DeleteModel(
            name='RelationShip',
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(through='relationships.Table', to='relationships.Course'),
        ),
    ]
