from rest_framework.views import APIView#, Response, status

class ExampleView(APIView):

    def post(self, request, *args, **kwargs):
        #body = request.data
        #return Response({"random_data":1}, status=status.HTTP_204_NO_CONTENT)

        raise NotImplementedError()

    def get(self, request, *args, **kwargs):
        # query_parameters = request.query_parameters

        # serializer = ExampleSerializer(instance=instance_you_retrieved, context={})
        # data = serializer.data

        raise NotImplementedError()

    def patch(self, request, *args, **kwargs):

        # serializer = ExampleSerializer(instance=instance_you_retrieved, data=data_you_retrieved, context={})
        # serializer.is_valid(raise_exception=True)
        # instance = serializer.save()
        # data = serializer.data

        raise NotImplementedError()

    def delete(self, request, *args, **kwargs):
        raise NotImplementedError()
