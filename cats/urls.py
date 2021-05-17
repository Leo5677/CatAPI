from rest_framework.routers import SimpleRouter
from .views import CatViewSet

""" 
Graças a utilização do ViewSet, conseguimos aplicar o SimpleRoute e facilitar a criação de nossas rotas. 
Em seguida, registramos nossa rota, passando como parâmetro nossa classe da view "CatViewSet"
"""
router = SimpleRouter()
router.register('cats', CatViewSet)
