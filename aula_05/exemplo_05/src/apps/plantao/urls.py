from django.urls import path
from .views import (
    home,
    criar,
    listagem,
    detalhes,
    alterar,
    deletar,
)

app_name = 'plantao'
urlpatterns = [
    path('', home, name='homepage'),
    path('criar/', criar, name='criar'),
    path('listar/', listagem, name='listar'),
    path('plantonista/<int:id>', detalhes, name='detalhes'),
    path('alterar/<int:id>', alterar, name='alterar'),
    path('apagar/<int:id>', deletar, name='deletar'),
]
