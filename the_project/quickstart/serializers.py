from rest_framework.serializers import ModelSerializer

class ExampleSerializer(ModelSerializer):

    class Meta:
        #model = ImportedModel
        fields = "__all__"
