# Generated by Django 4.1.1 on 2022-09-11 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_produtor', '0002_rename_area_1_produtor_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtor',
            name='area',
        ),
        migrations.RemoveField(
            model_name='produtor',
            name='cultura',
        ),
        migrations.CreateModel(
            name='ProdutorCultura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cultura', models.CharField(max_length=30)),
                ('area', models.IntegerField()),
                ('produtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro_produtor.produtor')),
            ],
        ),
    ]
