import json
from car.serializers import CarSerializer
from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    serialized_car = CarSerializer(car)
    return json.dumps(serialized_car).encode("utf-8")


def deserialize_car_object(car_json: bytes) -> Car:
    data = json.loads(car_json.decode("utf-8"))
    serialized_car = CarSerializer(data=data)
    serialized_car.is_valid(raise_exception=True)
    return Car(**serialized_car.validated_data)
