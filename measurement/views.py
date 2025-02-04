# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
import psycopg2


class CreateSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def create_sensor(self, request):
        sensor_name = request.POST.get('sensor_name')
        description = request.POST.get('description')
        Sensor(sensor_name=sensor_name, description=description).save()
        return Response({'status': 'Датчик добавлен'})


class ChangeSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class CreateMeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def create_measurement(self, request):
        sensor = request.POST.get('sensor')
        temperature = request.POST.get('temperature')
        MeasurementSerializer(sensor=sensor, temperature=temperature).save()
        return Response({'status': 'Измерение добавлено'})


class SensorDetailsView(RetrieveAPIView):
    queryset = Sensor.objects.all().prefetch_related('sensor')
    serializer_class = SensorDetailSerializer