import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from login.models import Person, Student, PosGradStudent, Professional
from login.paymentsUtils import attPrefferences, getCoursePrefferences, getCoursePrefferencesDesconto, getCoursePrefferencesDescontoCombo
from .forms import uploadFileForm

def loginHandler(request):
    if request.user.is_authenticated:
        check_completion(request)           
        return redirect('/auth/area-do-usuario/')
    
    if request.method == 'GET':
        return render(request, 'login.html')       
    if request.method == 'POST':
        cpf = request.POST.get('login-cpf')
        senha = request.POST.get('login-senha')
        
        try:
            person = Person.objects.get(cpf=cpf)
            username = person.user.username
            user = authenticate(username=username, password=senha)
            
            if user:
                django_login(request, user)
                return redirect('/auth/area-do-usuario/')
        except Person.DoesNotExist:
            pass
        
        return render(request, 'login.html', {'error': 'Senha ou CPF incorretos'})
    


def logoutHandler(request):
    django_logout(request)
    return redirect('/auth/login/')

def newPassword(request):
    return render(request, 'login.html', {'error': 'Recuperar senha'})

@login_required(login_url='/auth/login/')
def userArea(request):
    check_completion(request)
    
    user_data = Person.objects.get(user = request.user)
    
    form = uploadFileForm()
    
    context= {
        'form' : form,
        'nomecracha' : user_data.id_name,
        'cpf' : user_data.cpf,
        'email' : user_data.email,
        'telefone' : user_data.phone,
        'cidade' : user_data.city,
        'estado' : user_data.state,
        'user_type' : user_data.person_type,
        'payed' : 'True',
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
            'empresa' : user_type.enterprise_name,
        })
    
    if user_data.payed == False:
        preferenceId = attPrefferences(user_data.person_type)
        context.update({
            'payed' : 'False',
            'preferenceId' : preferenceId,
        })
    
    return render(request, 'user_space.html', context)

def register_user_step(request):
    if request.method == 'GET':
        return render(request, 'signup_step_one.html')
    if request.method == 'POST':
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
            
            return redirect('new-person')
            
        except:
            return render(request, 'signup_step_one.html', {'error' : 'Erro no cadastro do usuário'})
      
def check_cpf(request):
    if request.method == 'POST':
        cpf_fields = ['cpf1', 'cpf2', 'cpf3', 'cpf4']
        cpf_exists = {}
        emails = {}

        for cpf_field in cpf_fields:
            cpf = request.POST.get(cpf_field)
            if cpf:
                user = Person.objects.filter(cpf=cpf).first()
                if user:
                    cpf_exists[cpf_field] = True
                    emails[cpf_field] = user.email 
                else:
                    cpf_exists[cpf_field] = False
                    emails[cpf_field] = None
            else:
                cpf_exists[cpf_field] = False
                emails[cpf_field] = None

        all_exist = all(cpf_exists.values())

        if all_exist:
            return JsonResponse({'success': True, 'emails': emails})
        else:
            return JsonResponse({'success': False, 'error': 'Um ou mais CPFs não estão em nosso sistema', 'emails': emails})
    else:
        return JsonResponse({'success': False, 'error': 'Método de solicitação inválido', 'emails': emails})

@login_required(login_url='/auth/login/')
def register_person_step(request):
    if request.method == 'GET':
        return render(request, 'signup_step_two.html')
    if request.method == 'POST':
        try:
            cpf = request.POST.get('cpf')
            complete_name = request.POST.get('nome-completo')
            id_name = request.POST.get('nome-cracha')
            phone = request.POST.get('celular')
            city = request.POST.get('cidade')
            state = request.POST.get('estado')
            if request.POST.get('deficiencia') == 'on':
                is_deficient = 1
            else:
                is_deficient = 0
            deficiency = request.POST.get('descricao-deficiencia')
            person_type = request.POST.get('categoria')
            email = request.user.email
            
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
                        email = email,
                    )
            new_user.save()
            return redirect('new-person-type')
        except:
            return render(request, 'signup_step_two.html', {'error' : 'Erro no cadastro do usuário'})
        
@login_required(login_url='/auth/login/')
def register_person_type_step(request):
    user_data = Person.objects.get(user = request.user)
    if request.method == 'GET':
        return render(request, 'signup_step_three.html', {'person_type' : user_data.person_type})
    if request.method == 'POST':
        
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
                    course_id = request.FILES['comprovante-matricula'],
                )
                new_user.save()

            if user_data.person_type == 3:
                new_user = Professional(
                    data= user_data,
                    enterprise_name = request.POST.get('empresa'),
                    enterprise = request.POST.get('classificacao-empresa'),
                )
                new_user.save()
                
            return redirect('login')
        except:
            return render(request, 'signup_step_three.html', {'error' : 'Erro no cadastro do usuário'})
            
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
    

def paymentSuccess(request):
    person = Person.objects.get(user=request.user)

    person.payed = True
    person.save()
    
    subject = 'Confirmação de Pagamento'
    message = f'Olá {person.user.first_name},\n\nSeu pagamento foi confirmado com sucesso. Obrigado por sua compra!'

    verified_emails = json.loads(request.POST.get('verifiedEmails', '{}'))
    
    recipient_list = list(verified_emails.values())
    
    recipient_list.append(person.user.email)

    """ if recipient_list:
        send_mail(subject, message, 'from@example.com', recipient_list) """
    
    return redirect('area-do-usuario')

def paymentFailure(request):
    return redirect('login')

def paymentPendings(request):
    return redirect('login')

def updateWork(request):
    if request.method == 'POST':
        form = uploadFileForm(request.POST, request.FILES)
        if form.is_valid:
            file = request.FILES['file']
            person = Person.objects.get(user = request.user)
            person.work = file
            person.save()
        return redirect('area-do-usuario')

@login_required(login_url='/auth/login/')
def promotion(request):
    if request.method == 'POST':
        user_data = Person.objects.get(user = request.user)
        preferenceId = attPrefferences(user_data.person_type, True, request.POST.get('new_quantity'))
    pass

@login_required(login_url='/auth/login/')
def subscriptions(request):
    if request.method == 'POST':
        courses = list(request.POST.keys())
        if not courses:
            return redirect('login')  # Verifica se há cursos antes de prosseguir

        courses.pop(0)  # Remove o primeiro item se não for relevante
        
        # Verificar se a lista de cursos está vazia
        if not courses:
            return redirect('login')

        try:
            names = getCourseNames(courses)
            values = getCourseValues(courses)
            time = getCourseTime(courses)
        except IndexError as e:
            # Lidar com o erro de índice fora dos limites
            print(f"Erro ao acessar os valores dos cursos: {e}")
            return redirect('login')
        
        courses_list = []
        total = 0
        
        checkIfAlreadySubscripted(request)
        
        for index in range(len(names)):
            courses_list.append([names[index], time[index], values[index]])
            total += int(values[index])
            
        preferenceId = getCoursePrefferences(total)

        # Aplicar desconto
        user_data = Person.objects.get(user=request.user)
        value = 0
        if user_data.person_type == 1:
            value = 70.0
        elif user_data.person_type == 2:
            value = 90.0
        elif user_data.person_type == 3:
            value = 120.0
        desconto = 0.9 * (total + value)
        preferenceDesconto = getCoursePrefferencesDesconto(desconto)
        
        updateSubscription(request, names)

        context = {
            'courses': courses_list,
            'preferenceId': preferenceId,
            'preferenceDesconto': preferenceDesconto,
            'total': total,
            'desconto': desconto,
            'payed': user_data.payed,
        }
        
        return render(request, 'signup_payment.html', context)
    return redirect('login')

@login_required(login_url='/auth/login/')
def subscriptions_combo(request):
    if request.method == 'POST':
        print("============================", request.POST.get('cpf1'))

        courses = list(request.POST.keys())
        if not courses:
            return redirect('login')  # Verifica se há cursos antes de prosseguir

        courses.pop(0)  # Remove o primeiro item se não for relevante
        
        # Verificar se a lista de cursos está vazia
        if not courses:
            return redirect('login')

        try:
            names = getCourseNames(courses)
            values = getCourseValues(courses)
            time = getCourseTime(courses)
        except IndexError as e:
            # Lidar com o erro de índice fora dos limites
            print(f"Erro ao acessar os valores dos cursos: {e}")
            return redirect('login')
        
        courses_list = []
        total = 0
        
        checkIfAlreadySubscripted(request)
        
        for index in range(len(names)):
            courses_list.append([names[index], time[index], values[index]])
            total += int(values[index])
            
        
        preferenceId = getCoursePrefferences(total)

        # Aplicar desconto
        user_data = Person.objects.get(user=request.user)
        value = 0
        if user_data.person_type == 1:
            value = 70.0
        elif user_data.person_type == 2:
            value = 90.0
        elif user_data.person_type == 3:
            value = 120.0

        desconto = 0.9 * (total + value)
        preferenceDescontoCombo = getCoursePrefferencesDescontoCombo(desconto)

        combo = 5 * desconto

        updateSubscription(request, names)

        context = {
            'courses': courses_list,
            'preferenceId': preferenceId,
            'preferenceDescontoCombo': preferenceDescontoCombo,
            'total': combo,
            'desconto': combo,
            'payed': user_data.payed,
            'combo': True,
        }
        
        return render(request, 'signup_payment.html', context)
    return redirect('login')


def getCourseNames(courses):
    names = []
    for course in courses:
        names.append(course.split('|')[0])
    return names

def getCourseTime(courses):
    time = []
    for course in courses:
        time.append(course.split('|')[1])
    return time

def getCourseValues(courses):
    values = []
    for course in courses:
        values.append(course.split('|')[2])
    return values

def checkIfAlreadySubscripted(request):
    person = Person.objects.get(user = request.user)
    subscriptions = json.loads(person.subscripted_courses)
    for name in subscriptions:
        if subscriptions.get(name) == 'paid':
            return redirect('login')
        
def updateSubscription(request, names):
    person = Person.objects.get(user = request.user)
    subscriptions = json.loads(person.subscripted_courses)
    subscriptions = cleanUnpaidSubscriptions(subscriptions)
            
    for name in names:
        subscriptions.update({name: 'not_paid'})
        
    person.subscripted_courses = json.dumps(subscriptions)
    person.save()
    
@login_required(login_url='/auth/login/')
def updateSuccessPaidSubscription(request):
    person = Person.objects.get(user = request.user)
    subscriptions = json.loads(person.subscripted_courses)
    for name in subscriptions:
        subscriptions.update({name: 'paid'})
    person.subscripted_courses = json.dumps(subscriptions)
    person.save()
    redirect('area-do-usuario')
    
@login_required(login_url='/auth/login/')
def updateFailedPaidSubscription(request):
    person = Person.objects.get(user = request.user)
    subscriptions = json.loads(person.subscripted_courses)
    cleanUnpaidSubscriptions(subscriptions)
    person.subscripted_courses = json.dumps(subscriptions)
    person.save()
    redirect('area-do-usuario')
    
def cleanUnpaidSubscriptions(subscriptions):
    new_subscriptions = {}
    for name in subscriptions:
        if subscriptions.get(name) == 'paid':
            new_subscriptions.update({name: 'paid'})
    return new_subscriptions

@login_required(login_url='/auth/login/')
def updatePaymentSubscriptionComboSuccess(request):
    pass

@login_required(login_url='/auth/login/')
def updatePaymentSubscriptionSuccess(request):
    person = Person.objects.get(user = request.user)
    person.payed = True

    subscriptions = json.loads(person.subscripted_courses)
    for name in subscriptions:
        subscriptions.update({name: 'paid'})
    person.subscripted_courses = json.dumps(subscriptions)

    person.save()
    return redirect('area-do-usuario')

@login_required(login_url='/auth/login/')
def getCPF(request):
    if request.method == 'POST':
        nome1 = request.POST.get('nome1')
        cpf1 = request.POST.get('cpf1')
        person1 = Person.objects.filter(cpf__contains=cpf1, complete_name__contains=nome1)
        pessoa1 = [(p.complete_name, p.cpf) for p in person1]
        
        nome2 = request.POST.get('nome2')
        cpf2 = request.POST.get('cpf2')
        person2 = Person.objects.filter(cpf__contains=cpf2, complete_name__contains=nome2)
        pessoa2 = [(p.complete_name, p.cpf) for p in person2]
        
        nome3 = request.POST.get('nome3')
        cpf3 = request.POST.get('cpf3')
        person3 = Person.objects.filter(cpf__contains=cpf3, complete_name__contains=nome3)
        pessoa3 = [(p.complete_name, p.cpf) for p in person3]
        
        nome4 = request.POST.get('nome4')
        cpf4 = request.POST.get('cpf4')
        person4 = Person.objects.filter(cpf__contains=cpf4, complete_name__contains=nome4)
        pessoa4 = [(p.complete_name, p.cpf) for p in person4]
        
        # Apenas para verificar se está retornando os dados corretos
        print("=====================================================", pessoa1, pessoa2, pessoa3, pessoa4)

        return redirect('area-do-usuario') 

    
""" def send_custom_email(subject, message, recipient_list, from_email=None, fail_silently=False):
    if from_email is None:
        from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(subject, message, from_email, recipient_list, fail_silently=fail_silently) """
