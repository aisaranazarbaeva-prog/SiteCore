from rest_framework import serializers
from .models import StudyApplication, JobApplication, Contact

class StudyApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyApplication
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'




