from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from api import views

schema_view = get_swagger_view(title='Job API')

urlpatterns = [
    path('jobs', views.JobList.as_view()),
    path('swagger/', schema_view),
 ]
