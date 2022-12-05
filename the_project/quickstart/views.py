# see https://www.django-rest-framework.org/ for more info
# some example/pseudo is written below

from rest_framework.views import APIView

class ExampleView(APIView):

    def post(self, request, *args, **kwargs):
        raise NotImplementedError()

    def get(self, request, *args, **kwargs):
        raise NotImplementedError()

    def patch(self, request, *args, **kwargs):
        raise NotImplementedError()

    def delete(self, request, *args, **kwargs):
        raise NotImplementedError()

example_view = ExampleView.as_view()
