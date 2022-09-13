# Generated by Django 4.1.1 on 2022-09-13 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_produtor', '0004_produtor_area1_produtor_area2_produtor_area3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtor',
            name='cultura1',
            field=models.CharField(blank=True, choices=[('soja', 'Soja'), ('milho', 'Milho'), ('café', 'Café'), ('algodao', 'Algodao')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='produtor',
            name='cultura2',
            field=models.CharField(blank=True, choices=[('soja', 'Soja'), ('milho', 'Milho'), ('café', 'Café'), ('algodao', 'Algodao')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='produtor',
            name='cultura3',
            field=models.CharField(blank=True, choices=[('soja', 'Soja'), ('milho', 'Milho'), ('café', 'Café'), ('algodao', 'Algodao')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='produtor',
            name='cultura4',
            field=models.CharField(blank=True, choices=[('soja', 'Soja'), ('milho', 'Milho'), ('café', 'Café'), ('algodao', 'Algodao')], default=None, max_length=30, null=True),
        ),
    ]