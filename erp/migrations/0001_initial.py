# Generated by Django 3.1.2 on 2020-11-12 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('usn', models.CharField(max_length=30)),
                ('semester', models.CharField(max_length=10)),
                ('total_marks', models.IntegerField()),
                ('obtained_marks', models.IntegerField()),
            ],
        ),
    ]
