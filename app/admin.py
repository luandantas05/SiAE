from django.contrib import admin

from  .models import User, Aluno, Professor, Disciplina, Notas

admin.site.register(User)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Notas)