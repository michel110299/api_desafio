from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db.models.fields import IntegerField

class UsuarioManager(BaseUserManager):
    def create_user(self, email,cpf, nome, sobrenome, password=None, **kwargs):
        if not email:
            raise ValueError('Insira um e-mail para continuar!')
        if not nome:
            raise ValueError('Insira um nome para continuar!')
        if not sobrenome:
            raise ValueError('Insira um sobrenome para continuar!')

        usuario = self.model(
            cpf=cpf,
            email=email,
            nome=nome,
            sobrenome=sobrenome,
            **kwargs
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False
        if password: usuario.set_password(password)

        usuario.save()
        return usuario

    def create_superuser(self, email, cpf , nome, sobrenome, password, **kwargs):
        usuario = self.create_user(
            cpf=cpf,
            email=email,
            nome=nome,
            sobrenome=sobrenome,
            password=password,
            **kwargs
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.set_password(password)

        
        usuario.save()
        
        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    GENERO =[
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outro"),
        ("P", "Prefiro não dizer"),
    ]

    nome = models.CharField(verbose_name = 'Nome', max_length = 194, blank = True, null = True)
    sobrenome = models.CharField(verbose_name = 'Sobrenome', max_length = 194, blank = True, null = True)
    genero = models.CharField(verbose_name = 'Genero', max_length = 1, choices = GENERO, blank = True, null = True)
    cpf = models.CharField(verbose_name = 'CPF', max_length = 14, unique = True, blank = True, null = True)
    rg = models.CharField(verbose_name = 'RG', max_length = 15, blank = True, null = True)
    dataNascimento = models.DateField(verbose_name = 'Data de Nascimento', auto_now_add = False, blank = True, null = True)
    email = models.EmailField(verbose_name = 'E-mail', unique = True,blank=True,null=True)
    cep = models.CharField(verbose_name = 'CEP', max_length = 9,  blank = True, null = True)
    bairro = models.CharField(verbose_name = 'Bairro', max_length = 50, blank = True, null = True)
    logradouro = models.CharField(verbose_name = 'Logradouro', max_length = 100, blank = True, null = True)
    complemento = models.CharField(verbose_name = 'Complemento', max_length = 50, null = True, blank = True)
    numeroResidencia = models.CharField(verbose_name = 'Número da residência', max_length = 10, blank = True, null = True)   
    telefone = models.CharField(verbose_name = 'Telefone', max_length = 16, null = True, blank = True, )
    numeroCelular = models.CharField(verbose_name = 'Celular', max_length = 17, null = True, )
    idGroup = models.IntegerField(verbose_name = 'Id do grupo', default = 3)
    dataHorarioCriacao = models.DateTimeField(verbose_name = 'Data e hora de criação', auto_now_add = True)
    dataDesativacao = models.DateTimeField(verbose_name = 'Data e hora da desativação', blank = True, null = True)
    is_active = models.BooleanField(verbose_name = "Usuário está ativo")
    is_staff = models.BooleanField(verbose_name = "Usuário é da equipe de desenvolvimento", default = False)
    is_superuser = models.BooleanField(verbose_name = "Usuário é um superusuario", default = False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['nome', 'sobrenome', 'cpf']

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Carro(models.Model):
    nome = models.CharField(verbose_name = 'Nome', max_length = 194, blank = True, null = True)
    cor = models.CharField(verbose_name = 'Cor', max_length = 194, blank = True, null = True)
    ano = models.IntegerField(verbose_name = 'Ano' )

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"

    def __str__(self):
        return self.nome