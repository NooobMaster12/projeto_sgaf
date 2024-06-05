from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SerieForm, TurmaForm, NovaAulaForm, FrequenciaForms
from django.contrib import messages
from .models import Serie, Turma, Aula, FrequenciaDoAluno
from rolepermissions.decorators  import has_permission_decorator
# Create your views here.

'''
VIEWS PARA SERIE

'''

'''
Function Based View para criar uma nova serie na empresa
'''


@login_required
@has_permission_decorator('cadastrar_nova_serie')
def cadastrar_nova_serie(request):
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            serie = form.save(commit=False)
            serie.empresa = request.user.funcionario.empresa  
            serie.save()
            messages.success(request, "Série criada com sucesso!")
            return redirect('listar-series')  
    else:
        form = SerieForm() 

    context = {'form': form}
    return render(request, 'empresa/cadastrar-serie.html', context)


'''
Function Based View para listar todos os setores na minha empresa
'''

@login_required
@has_permission_decorator('listar_series') 
def listar_series(request):
    template_name = 'empresa/lista_de_series.html'
    empresa = request.user.funcionario.empresa
    series = Serie.objects.filter(instituicao=empresa)       
    context = {
        'series': series,
    }
    return render(request, template_name, context)

'''
Function Based View para atualizar uma serie da minha empresa
'''


@login_required
@has_permission_decorator('atualizar_serie') 
def atualizar_serie(request, id):
    empresa = request.user.funcionario.empresa
    serie = get_object_or_404(Serie, id=id, instituicao=empresa)
    template_name = 'empresa/atualizar-serie.html'
    
    if request.method == "POST":
        form = SerieForm(request.POST, instance=serie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Série atualizada com sucesso!')
            return redirect('listar-series') 
    else:
        form = SerieForm(instance=serie)
    
    return render(request, template_name, {'form': form})


'''
Function Based View para detalhar uma serie da minha empresa
'''

@login_required
@has_permission_decorator('detalhar_serie') 
def detalhar_serie(request, id):
    empresa = request.user.aluno.empresa
    serie = get_object_or_404(Serie, instituicao=empresa, id=id)
    return render(request, 'empresa/detalhar-serie.html', {'serie': serie})

'''
Function Based View para detalhar uma serie da minha empresa
'''

@login_required
@has_permission_decorator('deletar_serie') 
def deletar_serie(request, id):
    empresa = request.user.funcionario.empresa
    serie = get_object_or_404(Serie, instituicao=empresa, id=id)
    serie.delete()
    messages.success(request, 'Aluno deletado com sucesso!')
    return redirect('listar-series')

'''
VIEWS PARA TURMA

'''

'''
Function Based View para criar uma turma na empresa
'''


@login_required
def criar_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST, empresa=request.user.funcionario.empresa)
        if form.is_valid():
            turma = form.save(commit=False)
            turma.instituicao = request.user.funcionario.empresa
            turma.save()
            form.save_m2m() 
            return redirect('listar-turmas')
    else:
        form = TurmaForm(empresa=request.user.funcionario.empresa)
        
    return render(request, 'empresa/criar_turma.html', {'form': form})


'''
Function Based View para listar todos as turmas na minha empresa
'''

@login_required
def listar_turmas(request):
    template_name = 'empresa/lista_de_turmas.html'
    empresa = request.user.funcionario.empresa
    turmas = Turma.objects.filter(instituicao=empresa)       
    context = {
        'turmas': turmas,
    }
    return render(request, template_name, context)


'''
Function Based View para detalhar uma turma da minha empresa
'''

@login_required
def detalhar_turma(request, id):
    empresa = request.user.aluno.empresa
    turma = get_object_or_404(Turma, instituicao=empresa, id=id)
    return render(request, 'empresa/detalhar-turma.html', {'turma': turma})


'''
Function Based View para deletar uma turma da minha empresa
'''

@login_required
def deletar_turma(request, id):
    empresa = request.user.funcionario.empresa
    turma = get_object_or_404(Turma, instituicao=empresa, id=id)
    turma.delete()
    messages.success(request, 'Turma deletada com sucesso!')
    return redirect('listar-turmas')

'''
Function Based View para atualizar uma turma da minha empresa
'''

@login_required
def atualizar_turma(request, id):
    empresa = request.user.funcionario.empresa
    turma = get_object_or_404(Turma, id=id, instituicao=empresa)
    template_name = 'empresa/atualizar-turma.html'
    
    if request.method == "POST":
        form = TurmaForm(request.POST, instance=turma, empresa=request.user.funcionario.empresa)
        if form.is_valid():
            form.save()
            form.save_m2m() 
            messages.success(request, 'Turma atualizada com sucesso!')
            return redirect('listar-turmas') 
    else:
        form = TurmaForm(instance=turma, empresa=request.user.funcionario.empresa)
    
    return render(request, template_name, {'form': form})


'''
VIEWS PARA AULA

'''

def cadastrar_nova_aula(request):
    if request.method == 'POST':
        form = NovaAulaForm(request.POST)
        if form.is_valid():
            aula = form.save(commit=False)
            aula.instituicao = request.user.funcionario.empresa
            aula.save()
            messages.success(request, "Setor criado com sucesso!")
            return redirect('dashboard')
    else:
        form = NovaAulaForm()
    return render(request, 'empresa/nova-aula.html', {'form': form}) 


def listar_todas_aulas(request):
    template_name = 'empresa/listar-aulas.html'
    instituicao = request.user.funcionario.empresa
    aulas = Aula.objects.filter(instituicao=instituicao)
    return render(request, template_name, {'aulas': aulas})

    
def detalhar_aula(request, id):
    template_name = 'empresa/detalhar-aula.html'
    instituicao = request.user.funcionario.empresa
    aula = get_object_or_404(Aula, id=id, instituicao=instituicao)
    return render(request, template_name, {'aula': aula})
    
    
def atualizar_aula(request, id):    
    instituicao = request.user.funcionario.empresa
    aula = get_object_or_404(Aula, id=id, instituicao=instituicao)
    template_name = 'empresa/atualizar_aula.html'
    
    if request.method == "POST":
        form = NovaAulaForm(request.POST, instance=aula)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aula atualizada com sucesso!')
            return redirect('listar-aulas')
    else:
        form = NovaAulaForm(instance=aula)
    
    return render(request, template_name, {'form': form})



def deletar_aula(request, id):
    empresa = request.user.funcionario.empresa
    aula = get_object_or_404(Aula, instituicao=empresa, id=id)
    aula.delete()
    messages.success(request, 'Aula deletada com sucesso!')
    return redirect('listar-aulas')
    

'''
VIEWS PARA FREQUÊNCIA DE ALUNOS
'''
# @login_required
# @has_permission_decorator('criar_frequencia_aluno')
# def criar_frequencia_aluno(request):
#     if request.method == 'POST':
#         form = FrequenciaForms(request.POST, empresa=request.user.aluno.empresa)
#         if form.is_valid():
#             frequencia = form.save(commit=False)
#             frequencia.instituicao = request.user.aluno.empresa
#             frequencia.save()
#             messages.success(request, 'Frequência criada com sucesso!')
#             return redirect('listar-frequencia')
#         else:
#             form = FrequenciaForms()
#         return render(request, 'professor/criar-frequencia-aluno.html', {'form':form})
    

@login_required
@has_permission_decorator('listar_frequencias')
def listar_frequencias(request):
    template_name = 'listar_frequencia.html'
    empresa = request.user.aluno.empresa
    frequencias = FrequenciaDoAluno.objects.filter(instituicao=empresa)
    context = {
        'frequencias':frequencias,
    }
    return render(request, template_name, context)


@login_required
@has_permission_decorator('detalhar_frequencia')
def detalhar_frequencia(request, id):
    empresa = request.user.aluno.empresa
    frequencia = get_object_or_404(FrequenciaDoAluno, instituicao=empresa, id=id)
    return render(request, 'detalhar-frequencia', {'frequencia':frequencia})


@login_required
@has_permission_decorator('atualizar_frequencia')
def atualizar_frequencia(request, id):
    instituicao = request.user.aluno.empresa
    aluno = get_object_or_404(FrequenciaDoAluno, id=id, instituicao=instituicao)
    template_name = 'atualizar-frequencia.html'

    if request.tmethod == 'POST':
        form = FrequenciaForms(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Frequência atualizada com sucesso!')
            return redirect('listar_frequencias')
        else:
            form = FrequenciaForms(instance=aluno)
        return render(request, template_name, {'form':form})







    
