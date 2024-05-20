from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

from login.models import Person, Student, PosGradStudent, Professional

def registerHandler(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    if request.method == 'POST':
        username = request.POST.get('login-username')
        user = User.objects.filter(username=username.lower()).first()
        if user:
            return render(request, 'cadastro.html', {'error': 'Já existe um usuário com esse nome'})
        
        email = request.POST.get('email')     
        senha = request.POST.get('senha1')
        cpf = request.POST.get('cpf')
        complete_name = request.POST.get('complete_name')
        id_name = request.POST.get('id_name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        is_deficient = request.POST.get('is_deficient')
        deficiency = request.POST.get('deficiency')
        person_type = request.POST.get('person_type')
        
        try:
            user = User.objects.create_user(username=username, email=email, password=senha)
            user.save()
            
            new_user = Person(
                user = user,
                cpf = cpf,
                complete_name = complete_name.capitalize(),
                id_name = id_name.complete_name.capitalize(),
                phone = phone,
                city = city,
                state = state,
                is_deficient = is_deficient,
                deficiency = deficiency,
                person_type = person_type,
            )
            new_user.save()

            if person_type == 1:
                new_upper_user = Student(
                    data= new_user,
                    course = request.POST.get('course')
                )
                new_upper_user.save()
 
            if person_type == 2:
                new_upper_user = PosGradStudent(
                    data= new_user,
                    area = request.POST.get('area'),
                    institution = request.POST.get('institution'),
                    course_id = request.POST.get('course_id'),
                )
                new_upper_user.save()
                
            if person_type == 3:
                new_upper_user = Professional(
                    data= new_user,
                    enterprise = request.POST.get('enterprise')
                )
                new_upper_user.save()
        except:
            return render(request, 'cadastro.html', {'error': 'Houve um erro ao cadastrar o usuário, tente novamente'})
        
        return render(request, 'login.html', {'error': 'Usuário cadastrado'})

def loginHandler(request):
    if request.user.is_authenticated:
        return redirect('/auth/area-do-usuario/')
    
    if request.method == 'GET':
        return render(request, 'login2.html')       
    if request.method == 'POST':
        username = request.POST.get('login-username')      
        senha = request.POST.get('login-senha')
        
        user = authenticate(username=username.lower(), password=senha)
        
        if user:
            django_login(request, user)
            
            return redirect('/auth/area-do-usuario/')
        
        return render(request, 'login2.html', {'error': 'Senha ou nome incorretos'})

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
            'matricula': user_type.course_id,
        })
    if user_data.person_type == 3:
        user_type = Professional.objects.get(data=user_data)
        context.update({
            'empresa' : user_type.enterprise,
        })
    
    return render(request, 'user_space.html', context)