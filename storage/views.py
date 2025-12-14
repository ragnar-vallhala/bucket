from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import Bucket, Object

class ObjectView(APIView):

    def get(self, request, bucket_name, key):
        obj = get_object_or_404(
            Object,
            bucket__name=bucket_name,
            key=key
        )
        return FileResponse(obj.file.open(), as_attachment=False)

    def put(self, request, bucket_name, key):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file"}, status=400)

        bucket, _ = Bucket.objects.get_or_create(name=bucket_name)

        obj, _ = Object.objects.update_or_create(
            bucket=bucket,
            key=key,
            defaults={"file": file}
        )

        return Response({
            "bucket": bucket.name,
            "key": obj.key,
            "url": obj.file.url
        })
