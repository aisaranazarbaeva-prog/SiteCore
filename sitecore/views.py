from rest_framework import generics
from rest_framework.response import Response
from .models import StudyApplication, JobApplication, Contact
from .serializers import StudyApplicationSerializer, JobApplicationSerializer, ContactSerializer
import requests
from django.conf import settings
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')



TELEGRAM_BOT_TOKEN = '7498325112:AAFhwU4r2e-d2XLGUcYliyJ44M16SdnkLOY'
TELEGRAM_CHAT_ID = '5396459602'

def send_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    requests.post(url, data={'chat_id': TELEGRAM_CHAT_ID, 'text': message})


class StudyApplicationCreate(generics.CreateAPIView):
    serializer_class = StudyApplicationSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        send_telegram(f"Новая заявка на обучение:\nФИО: {obj.full_name}\nТелефон: {obj.phone}\nEmail: {obj.email}")


class JobApplicationCreate(generics.CreateAPIView):
    serializer_class = JobApplicationSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        send_telegram(f"Новая заявка на работу:\nФИО: {obj.full_name}\nТелефон: {obj.phone}\nEmail: {obj.email}\nДолжность: {obj.desired_position}\nЗарплата: {obj.expected_salary}")


class ContactList(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
