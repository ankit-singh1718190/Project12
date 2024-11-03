from django.shortcuts import render
from .serializers import StudentSerializer
from .models import StudentModel
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def StudentDets(request):
    stu = StudentModel.objects.all() # Fetching the student with id=5
    serializer = StudentSerializer(stu,many=True) # Serializing the student object
    json_data = JSONRenderer().render(serializer.data)  # Rendering serialized data as JSON
    return HttpResponse(json_data, content_type='application/json')
