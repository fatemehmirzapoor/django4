from django.urls import path
from .views import main_list
from main import views
app_name = 'main'
urlpatterns = [
 # post views
    path('', main_list, name='main_list'),
#  path('<int:year>/<int:month>/<int:day>/<slug:post>/',
#  views.post_detail,
#  name='post_detail'),
]