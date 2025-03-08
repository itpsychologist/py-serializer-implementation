import io
import json
from rest_framework.parsers import JSONParser
from car.serializers import CarSerializer
from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    serialized_car = CarSerializer(car)
    return json.dumps(serialized_car.data, separators=(",", ":")).encode("utf-8")


def deserialize_car_object(car_json: bytes) -> Car:
    stream = io.BytesIO(car_json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
