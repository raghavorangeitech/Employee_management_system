from django.urls import path,include
from .views import converter


urlpatterns = [
     path('', converter, name='convert'),
]