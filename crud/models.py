from django.db import models

# Create your models here.

class agenda(models.Model):
    #nome

    nome = models.CharField(max_length=100)
    
    #telefone

    fone = models.CharField(max_length=20)

    #endereço

    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField(default = 0)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    # e-mail

    email= models.EmailField(max_length=254)

    #sexo

    sexo_choice = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    sexo = models.CharField(
        max_length = 1,
        choices = sexo_choice,
    )
    # data de nascimento

    data = models.CharField(
        max_length = 10)

def __str__(self):
    return self.nome

