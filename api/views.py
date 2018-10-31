from rest_framework import generics

# Create your views here.
from api.models import Job
from api.serializers import JobSerializer


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
