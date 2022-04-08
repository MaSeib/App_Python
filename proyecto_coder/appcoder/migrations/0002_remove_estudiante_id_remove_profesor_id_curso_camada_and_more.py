# Generated by Django 4.0.3 on 2022-04-06 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='id',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='id',
        ),
        migrations.AddField(
            model_name='curso',
            name='camada',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='curso',
            name='nombre',
            field=models.CharField(default='Python', max_length=40),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='entregable',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
