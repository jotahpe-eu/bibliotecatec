from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Cidade)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Livro)
admin.site.register(Emprestimo)