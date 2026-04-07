from django.urls import path
from . import views
 # The URL dispatcher (step 2 of the HTTP request flow from the lecture)
# routes the incoming URL to the correct view function.
urlpatterns = [
    path('', views.task_list, name='task_list'),
         ]