# Generated by Django 4.2.13 on 2024-05-28 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data da Aula')),
                ('horario_inicio', models.TimeField(blank=True, null=True, verbose_name='Horário de Início')),
                ('horario_termino', models.TimeField(blank=True, null=True, verbose_name='Horário de Término')),
                ('conteudo', models.TextField(blank=True, null=True, verbose_name='Conteúdo da Aula')),
                ('status', models.CharField(choices=[('AG', 'Agendada'), ('EA', 'Em andamento'), ('CO', 'Concluída'), ('CA', 'Cancelada')], default='SCHEDULED', max_length=10, verbose_name='Status da Aula')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.disciplina', verbose_name='Disciplina')),
            ],
            options={
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(choices=[('F11', '1º Ano'), ('F12', '2º Ano'), ('F13', '3º Ano'), ('F14', '4º Ano'), ('F15', '5º Ano'), ('F26', '6º Ano'), ('F27', '7º Ano'), ('F28', '8º Ano'), ('F29', '9º Ano')], max_length=3, verbose_name='Série da Turma')),
                ('turno', models.CharField(choices=[('M', 'Matutino'), ('T', 'Vespertino'), ('N', 'Noturno')], max_length=1, verbose_name='Turno da Turma')),
            ],
            options={
                'verbose_name': 'Série',
                'verbose_name_plural': 'Séries',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_letivo', models.PositiveSmallIntegerField(verbose_name='Ano Letivo')),
                ('nome_turma', models.CharField(choices=[('A', 'Turma A'), ('B', 'Turma B'), ('C', 'Turma C'), ('D', 'Turma D'), ('E', 'Turma E')], max_length=1, verbose_name='Nome da Turma')),
                ('status', models.CharField(choices=[('Iniciando', 'Iniciando'), ('Em andamento', 'Em andamento'), ('Férias', 'Férias'), ('Finalizada', 'Finalizada'), ('Suspensa', 'Suspensa')], default='Iniciando', max_length=20, verbose_name='Status da Turma')),
                ('alunos', models.ManyToManyField(related_name='alunos', to='core.aluno', verbose_name='Alunos')),
                ('disciplinas', models.ManyToManyField(related_name='disciplinas', to='core.disciplina', verbose_name='Disciplinas')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.empresa', verbose_name='Instituição')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.nivel', verbose_name='Nível da Série')),
                ('sala_de_aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.saladeaula', verbose_name='Sala de Aula')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='gestao_escolar.serie', verbose_name='series')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
            },
        ),
        migrations.CreateModel(
            name='FrequenciaDoAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presenca', models.BooleanField(default=True, verbose_name='Presença do Aluno')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.aluno', verbose_name='Aluno')),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.aula', verbose_name='Aula')),
            ],
            options={
                'verbose_name': 'Frequência do Aluno',
                'verbose_name_plural': 'Frequências do Aluno',
            },
        ),
        migrations.CreateModel(
            name='BoletimDoAlunoPorDisciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeira_nota_bimestre_um', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Nota da Prova 1')),
                ('segunda_nota_bimestre_um', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Nota da Prova 2')),
                ('recuperacao_bimestre_um', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Nota Recuperação do Bimestre 1')),
                ('primeira_nota_bimestre_dois', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Nota da Prova 3')),
                ('segunda_nota_bimestre_dois', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Nota da Prova 4')),
                ('recuperacao_bimestre_dois', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Nota Recuperação do Bimestre 2')),
                ('primeira_nota_bimestre_tres', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Nota da Prova 5')),
                ('segunda_nota_bimestre_tres', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Nota da Prova 6')),
                ('recuperacao_bimestre_tres', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Nota Recuperação do Bimestre 3')),
                ('primeira_nota_bimestre_quatro', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Nota da Prova 7')),
                ('segunda_nota_bimestre_quatro', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Nota da Prova 8')),
                ('recuperacao_bimestre_quatro', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Nota Recuperação do Bimestre 4')),
                ('media_anual', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Média Anual')),
                ('prova_final', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Prova Final do Anual')),
                ('status_aprovacao', models.CharField(blank=True, choices=[('APROVADO', 'Aprovado'), ('REPROVADO', 'Reprovado'), ('EM ANDAMENTO', 'Em Andamento')], max_length=15, null=True, verbose_name='Status de Aprovação')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.aluno', verbose_name='Aluno')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.disciplina', verbose_name='Disciplina')),
            ],
        ),
        migrations.AddField(
            model_name='aula',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.turma', verbose_name='Turma'),
        ),
    ]
