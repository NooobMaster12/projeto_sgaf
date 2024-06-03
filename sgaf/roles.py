from rolepermissions.roles import AbstractUserRole

class Aluno(AbstractUserRole):
    available_permissions = {
        'cadastrar_setor': False,
        'ver_setores': False,
        'atualizar_setor': False,
        'deletar_setor': False,
        'detalhar_setor': False,
        'novo_professor': False,
        'listar_professores': False,
        'atualizar_professor': False,
        'deletar_professor': False,
        'detalhar_professor': False,
        'novo_funcionario': False,
        'listar_funcionarios': False,
        'atualizar_funcionario': False,
        'deletar_funcionario': False,
        'detalhar_funcionario': False,
        'criar_aluno': False,
        'listar_alunos': False,
        'detalhar_aluno': False,
        'atualizar_aluno': False,
        'deletar_aluno': False,
        'criar_disciplina': False,
        'listar_disciplinas': False,
        'deletar_disciplina': False,
        'detalhar_disciplina': False,
        'atualizar_disciplina': False,
        'ativar_disciplina': False,
        'desativar_disciplina': False,
        'criar_sala_de_aula': False,
        'listar_salas_de_aula': False,
        'deletar_sala_de_aula': False,
        'detalhar_sala_de_aula': False,
        'atualizar_sala_de_aula': False,
        'marcar_sala_como_acessivel': False,
        'marcar_sala_como_inacessivel': False,
        'atualizar_dados_pessoais_aluno': True,
        'listar_disciplinas_aluno': True,
        'cadastrar_nova_serie': False,
        'listar_series': False,
        'atualizar_serie': False,
        'detalhar_serie': False,
        'deletar_serie': False,
        'consultar_frequencia_escolar_do_aluno': True,
        'consultar_minhas_notas_por_disciplina': True,
        'dashboard': False,
        'alterar_senha': True,
        'sair': True,
        'atualizar_dados_pessoais_professor': False,
    }
    
class Professor(AbstractUserRole):
    available_permissions = {
        'cadastrar_setor': False,
        'ver_setores': False,
        'atualizar_setor': False,
        'deletar_setor': False,
        'detalhar_setor': False,
        'novo_professor': False,
        'listar_professores': False,
        'atualizar_professor': False,
        'deletar_professor': False,
        'detalhar_professor': False,
        'novo_funcionario': False,
        'listar_funcionarios': False,
        'atualizar_funcionario': False,
        'deletar_funcionario': False,
        'detalhar_funcionario': False,
        'criar_aluno': False,
        'listar_alunos': False,
        'detalhar_aluno': False,
        'atualizar_aluno': False,
        'deletar_aluno': False,
        'criar_disciplina': False,
        'listar_disciplinas': False,
        'deletar_disciplina': False,
        'detalhar_disciplina': False,
        'atualizar_disciplina': False,
        'ativar_disciplina': False,
        'desativar_disciplina': False,
        'criar_sala_de_aula': False,
        'listar_salas_de_aula': False,
        'deletar_sala_de_aula': False,
        'detalhar_sala_de_aula': False,
        'atualizar_sala_de_aula': False,
        'marcar_sala_como_acessivel': False,
        'marcar_sala_como_inacessivel': False,
        'atualizar_dados_pessoais_aluno': False,
        'listar_disciplinas_aluno': False,
        'cadastrar_nova_serie': False,
        'listar_series': False,
        'atualizar_serie': False,
        'detalhar_serie': False,
        'deletar_serie': False,
        'consultar_frequencia_escolar_do_aluno': False,
        'consultar_minhas_notas_por_disciplina': False,
        'dashboard': False,
        'alterar_senha': True,
        'sair': True,
        'atualizar_dados_pessoais_professor': True,
    }
    
class Funcionario(AbstractUserRole):
    available_permissions = {
        'cadastrar_setor': True,
        'ver_setores': True,
        'atualizar_setor': True,
        'deletar_setor': True,
        'detalhar_setor': True,
        'novo_professor': True,
        'listar_professores': True,
        'atualizar_professor': True,
        'deletar_professor': True,
        'detalhar_professor': True,
        'novo_funcionario': True,
        'listar_funcionarios': True,
        'atualizar_funcionario': True,
        'deletar_funcionario': True,
        'detalhar_funcionario': True,
        'criar_aluno': True,
        'listar_alunos': True,
        'detalhar_aluno': True,
        'atualizar_aluno': True,
        'deletar_aluno': True,
        'criar_disciplina': True,
        'listar_disciplinas': True,
        'deletar_disciplina': True,
        'detalhar_disciplina': True,
        'atualizar_disciplina': True,
        'ativar_disciplina': True,
        'desativar_disciplina': True,
        'criar_sala_de_aula': True,
        'listar_salas_de_aula': True,
        'deletar_sala_de_aula': True,
        'detalhar_sala_de_aula': True,
        'atualizar_sala_de_aula': True,
        'marcar_sala_como_acessivel': True,
        'marcar_sala_como_inacessivel': True,
        'atualizar_dados_pessoais_aluno': False,
        'listar_disciplinas_aluno': False,
        'cadastrar_nova_serie': True,
        'listar_series': True,
        'atualizar_serie': True,
        'detalhar_serie': True,
        'deletar_serie': True,
        'consultar_frequencia_escolar_do_aluno': False,
        'consultar_minhas_notas_por_disciplina': False,
        'dashboard': True,
        'alterar_senha': True,
        'sair': True,
        'atualizar_dados_pessoais_professor': False,
    }