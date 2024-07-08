from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
import json


class CreateTaskView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        import pdb

        pdb.set_trace()
        if serializer.is_valid():
            task = serializer.save()
            return Response({"task_id": task.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PendingTasksView(APIView):
    def get(self, request):
        tasks = Task.objects.filter(status="pending").order_by("-created_at")
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateTaskView(APIView):

    def get(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response(
                {"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response(
                {"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND
            )
        # Save uploaded files
        file_paths = []
        for file_key in request.FILES:
            uploaded_file = request.FILES[file_key]
            file_path = default_storage.save(
                os.path.join("tasks", str(task_id), uploaded_file.name),
                ContentFile(uploaded_file.read()),
            )
            file_paths.append(default_storage.url(file_path))

        original_result = request.data.getlist("result")
        status_code = original_result[0] if original_result else ""
        new_result = {"status_code": status_code, "files": file_paths}
        data = request.data.dict()
        data.pop("image1", None)
        data.pop("image2", None)
        data.pop("result", None)

        data["result"] = json.dumps(new_result)

        serializer = TaskSerializer(task, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
