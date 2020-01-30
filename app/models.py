from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_aluno = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
    
    class Meta: 
        verbose_name_plural = "Professores"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='professor')
    alunos = models.ManyToManyField(Aluno, blank=True, related_name='alunos')

    def __str__(self):
        return self.nome

class Notas(models.Model):
    nota = models.FloatField()
    disciplina = models.ForeignKey(Disciplina,on_delete=models.CASCADE)

    class Meta: 
        verbose_name_plural = "Notas"
