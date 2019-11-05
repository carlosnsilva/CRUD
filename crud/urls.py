from django.urls import path
from .views import create, read, update, delete


urlpatterns =[
    path('', read, name='read'),
    path('cadastro', create, name = 'create'),
    path('update/<int:id>',update, name = 'update'),
    path('exluir/<int:id>', delete, name ='delete')
]