# see https://www.django-rest-framework.org/ for more info
# some example/pseudo is written below

from rest_framework.serializers import ModelSerializer

class ExampleSerializer(ModelSerializer):

    class Meta:
        #model = ExampleModel
        fields = "__all__"
