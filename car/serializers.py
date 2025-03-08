from rest_framework import serializers
from car.models import Car


class CarSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        validators=[serializers.MinValueValidator(1),
                    serializers.MaxValueValidator(1914)]
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
