# Generated by Django 4.1.7 on 2023-04-20 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ERole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Salary', models.IntegerField(default=0)),
                ('Bonus', models.IntegerField(default=0)),
                ('Phone', models.IntegerField(default=0)),
                ('HireDate', models.DateField()),
                ('Dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpApp.department')),
                ('Role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpApp.erole')),
            ],
        ),
    ]
