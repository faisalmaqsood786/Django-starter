from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse

class SendResponse(APIView):
    def get(self,request,):
        return JsonResponse({'foo': 'bar'})
        # return HttpResponse("Hello, world. You're at the polls index.")