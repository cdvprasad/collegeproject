# Generated by Django 4.0.5 on 2022-06-17 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branchapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branchapp.studentinfo')),
            ],
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
