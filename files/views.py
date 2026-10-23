from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileUploadSerializer
from rest_framework import status
from .tasks import process_file


# Create your views here.

class FileUploadView(APIView):

    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            uploaded_file=serializer.save(
                original_name=serializer.validated_data["file"].name
            )

            process_file.delay(uploaded_file.id)

            return Response(
                {"status": "Uploaded"},

                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

        