# myproject/healthcarebotbackend/urls.py
from django.urls import path
from .views import CreateTaskView, PendingTasksView, UpdateTaskView

urlpatterns = [
    path("tasks/create/", CreateTaskView.as_view(), name="create_task"),
    path("tasks/pending/", PendingTasksView.as_view(), name="pending_tasks"),
    path("tasks/update/<int:task_id>/", UpdateTaskView.as_view(), name="update_task"),
]
