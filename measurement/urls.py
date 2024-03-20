from django.urls import path
from .views import CreateSensorView, ChangeSensorView, CreateMeasurementView, SensorDetailsView


urlpatterns = [
    path('sensor/create/', CreateSensorView.as_view()),
    path('sensor/change/<pk>/', ChangeSensorView.as_view()),
    path('measurement/', CreateMeasurementView.as_view()),
    path('sensor/details/<pk>/', SensorDetailsView.as_view()),
]
