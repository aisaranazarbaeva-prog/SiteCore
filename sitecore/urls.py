from django.urls import path
from .views import StudyApplicationCreate, JobApplicationCreate, ContactList

urlpatterns = [
    path('study/', StudyApplicationCreate.as_view(), name='study'),
    path('job/', JobApplicationCreate.as_view(), name='job'),
    path('contacts/', ContactList.as_view(), name='contacts'),
]
