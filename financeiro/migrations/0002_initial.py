# Generated by Django 4.2.13 on 2024-05-28 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('financeiro', '0001_initial'),
        ('core', '__first__'),
        ('gestao_escolar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensalidade',
            name='serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.serie'),
        ),
        migrations.AddField(
            model_name='fatura',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.aluno'),
        ),
        migrations.AddField(
            model_name='fatura',
            name='valor_mensal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.mensalidade'),
        ),
    ]
