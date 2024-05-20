from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

from login.models import Person, Student, PosGradStudent, Professional

def loginHandler(request):
    if request.user.is_authenticated:
        check_completion(request)
        return redirect('/auth/area-do-usuario/')
    
    if request.method == 'GET':
        return render(request, 'login.html')       
    if request.method == 'POST':
        username = request.POST.get('login-username')
        senha = request.POST.get('login-senha')
        
        user = authenticate(username=username.lower(), password=senha)
        
        if user:
            django_login(request, user)
            
            return redirect('/auth/area-do-usuario/')
        
        return render(request, 'login.html', {'error': 'Senha ou nome incorretos'})

def logoutHandler(request):
    django_logout(request)
    return redirect('/auth/login/')

def newPassword(request):
    return render(request, 'login.html', {'error': 'Recuperar senha'})

@login_required(login_url='/auth/login/')
def userArea(request):
    
    user_data = Person.objects.get(user = request.user)
    
    context= {
        'nomecracha' : user_data.id_name,
        'cpf' : user_data.cpf,
        'email' : user_data.email,
        'telefone' : user_data.phone,
        'cidade' : user_data.city,
        'estado' : user_data.state,
        'user_type' : user_data.person_type, 
    }
    
    if user_data.person_type == 1:
        user_type = Student.objects.get(data=user_data)
        context.update({
            'curso' : user_type.course,
            'instituicao' : user_type.institution,
            'matricula': user_type.course_id,
        })
    if user_data.person_type == 2:
        user_type = PosGradStudent.objects.get(data=user_data)
        context.update({
            'area' : user_type.area,
            'instituicao' : user_type.institution,
        })
    if user_data.person_type == 3:
        user_type = Professional.objects.get(data=user_data)
        context.update({
            'empresa' : user_type.enterprise,
        })
    
    return render(request, 'user_space.html', context)

def register_user_step(request):
    username = request.POST.get('nome')
    user = User.objects.filter(username=username.lower()).first()
    
    if user:
        render(request, 'signup_step_one.html', {'error' : 'Já existe um usuário com esse nome'})
    
    email = request.POST.get('cadastro-email')
    senha = request.POST.get('cadastro-senha')
    
    try:
        user = User.objects.create_user(username=username.lower(), email=email, password=senha)
        user.save()
        
        user = authenticate(username=username.lower(), password=senha)
        django_login(request, user)
        
        render(request, 'signup_step_two.html')
        
    except:
        render(request, 'signup_step_one.html', {'error' : 'Erro no cadastro do usuário'})
        
def register_person_step(request):
    try:
        cpf = request.POST.get('cpf')
        complete_name = request.POST.get('nome-completo')
        id_name = request.POST.get('nome-cracha')
        phone = request.POST.get('celular')
        city = request.POST.get('cidade')
        state = request.POST.get('estado')
        is_deficient = request.POST.get('deficiencia')
        deficiency = request.POST.get('descricao-deficiencia')
        person_type = request.POST.get('categoria')
        
        new_user = Person(
                    user = request.user,
                    cpf = cpf,
                    complete_name = complete_name.capitalize(),
                    id_name = id_name.capitalize(),
                    phone = phone,
                    city = city,
                    state = state,
                    is_deficient = is_deficient,
                    deficiency = deficiency,
                    person_type = person_type,
                )
        new_user.save()
        render(request, 'signup_step_three.html', {'person_type': person_type})
    except:
        render(request, 'signup_step_two.html', {'error' : 'Erro no cadastro do usuário'})
    
def register_person_type_step(request):
    
    user_data = Person.objects.get(user = request.user)
    try:
        if user_data.person_type == 1:
            new_user = Student(
                data= user_data,
                course = request.POST.get('curso'),
                institution = request.POST.get('instituicao'),
                course_id = request.POST.get('matricula'),
            )
            new_user.save()

        if user_data.person_type == 2:
            new_user = PosGradStudent(
                data= user_data,
                area = request.POST.get('area-atuacao'),
                institution = request.POST.get('instituicao-pos'),
                course_id = request.POST.get('comprovante-matricula'),
            )
            new_user.save()

        if user_data.person_type == 3:
            new_user = Professional(
                data= user_data,
                enterprise_name = request.POST.get('empresa'),
                enterprise = request.POST.get('classificacao-empresa'),
            )
            new_user.save()
            
        render(request, 'signup_step_three.html', {'error' : 'Erro no cadastro do usuário'})
    except:
        render(request, 'signup_step_three.html', {'error' : 'Erro no cadastro do usuário'})
        
def check_completion(request):
    try:
        data = Person.objects.get(user = request.user)
        if data.person_type == 1:
            Student.objects.get(data=data)

        if data.person_type == 2:
            PosGradStudent.objects.get(data=data)

        if data.person_type == 3:
            Professional.objects.get(data=data)

    except:
        user = User.objects.get(username=request.user.username)
        django_logout(request)
        user.delete()
    