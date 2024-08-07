from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    """Clase que define uma pessoa em geral"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cpf = models.CharField("CPF", max_length=30, primary_key=True)
    complete_name = models.CharField(verbose_name="Nome completo", max_length=100)
    id_name = models.CharField(verbose_name="Nome no crachá", max_length=100)
    email = models.EmailField(verbose_name="E-mail", max_length=254)
    phone = models.CharField(verbose_name="Telefone", max_length=30)
    city = models.CharField(verbose_name="Cidade", max_length=30)
    state = models.CharField(verbose_name="UF", max_length=30)
    is_deficient = models.BooleanField(verbose_name="Tem deficiência?", default=False, null=True)
    deficiency = models.CharField(verbose_name="Qual a deficiência?", max_length=50, default="", blank=True)
    person_type = models.IntegerField(verbose_name="Tipo de Pessoa")
    date_added = models.DateTimeField(verbose_name="Dia em que foi cadastrado", auto_now_add=True, null=True)
    payed = models.BooleanField(verbose_name="Pago", default=False)
    work = models.FileField(verbose_name="Trabalho Submetido", upload_to="uploads/work/%Y/%m/%d/", blank=True, null=True)
    subscripted_courses = models.TextField(verbose_name="Mini Cursos Inscritos", default={})
    
    def __str__(self) -> str:
        """Retorna um representação em string do modelo."""
        return self.complete_name
    
class Student(models.Model):
    data = models.ForeignKey(Person, on_delete=models.CASCADE)
    course = models.CharField(verbose_name="Curso", max_length=100)
    institution = models.CharField(verbose_name="Instituição", max_length=100)
    course_id = models.CharField(verbose_name="Número de matrícula", max_length=50)

class PosGradStudent(models.Model):
    data = models.ForeignKey(Person, on_delete=models.CASCADE)
    area = models.CharField(verbose_name="Area de atuação", max_length=100)
    institution = models.CharField(verbose_name="Instituição", max_length=100)
    course_id = models.FileField(verbose_name="Comprovante de vínculo", upload_to="uploads/%Y/%m/%d/")

class Professional(models.Model):
    ENTERPRISE_TYPE = [
        ("MIN", "Mineradora"),
        ("FOR", "Fornecedora do Setor Mineral"),
        ("ACA", "Academia"),
        ("ONG", "ONG / Terceiro Setor"),
        ("POD", "Poder Público"),
        ("ENT", "Entidades"),
        ("CON", "Consultoria"),
        ("AUT", "Autônomo"),
        ("OUT", "Outros"),
    ]
    data = models.ForeignKey(Person, on_delete=models.CASCADE)
    enterprise_name = models.CharField(verbose_name="Nome da Empresa", max_length=100)
    enterprise = models.CharField(verbose_name="Empresa", max_length=3, choices=ENTERPRISE_TYPE)
    