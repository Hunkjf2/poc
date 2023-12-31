# Generated by Django 4.2.4 on 2023-08-09 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('cpf', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=250)),
                ('cargo', models.CharField(max_length=250)),
                ('departamentoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='department.department')),
            ],
        ),
    ]
