from rest_framework import serializers
from django.forms.models import model_to_dict
from .models import Planet


class PlanetSerializer(serializers.ModelSerializer):
    """
    Default serializer for the Planet model.
    """
    # Display if there are any planets orbiting this one.
    orbitors = serializers.SerializerMethodField('get_orbitors')

    def get_orbitors(self, model):
        orbitors = Planet.objects.filter(orbiting=model.name).values_list('name', flat=True).order_by('name')
        return list(orbitors)

    def validate(self, data):
        """
        Add server-side validation here. Since mass and volume are strings, we could e.g. check
        that they are numerical and non-negative.
        """
        orbiting = data.get('orbiting', None)

        if orbiting:
            try:
                Planet.objects.get(name=orbiting)
            except Planet.DoesNotExist:
                raise serializers.ValidationError("That planet orbit does not exist in the system.")

        return data

    class Meta:
        model = Planet
        fields = '__all__'
