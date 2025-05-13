from django.urls import path
from .views import predict_growth

urlpatterns = [
    path("", predict_growth, name="predict_growth"),
]
