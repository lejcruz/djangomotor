# Generated by Django 4.1.1 on 2022-09-15 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_ancora', '0002_rename_valor_cpf_cnpj_ancora_cpf_cnpj'),
        ('cadastro_produtor', '0007_rename_valor_cpf_cnpj_produtor_cpf_cnpj'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtor',
            name='ancora',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastro_ancora.ancora'),
        ),
    ]
