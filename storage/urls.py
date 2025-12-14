from django.urls import path
from .views import ObjectView

urlpatterns = [
    path('<str:bucket_name>/<path:key>', ObjectView.as_view()),
]
