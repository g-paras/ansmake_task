from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name="home"),
    path('task/all/', view=views.get_all_task, name="get-tasks"),
    path('task/new/', view=views.add_new_task, name="create-task")
]