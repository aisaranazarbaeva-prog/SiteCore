from django.db import models


class StudyApplication(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

class JobApplication(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    desired_position = models.CharField(max_length=100)
    expected_salary = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    email = models.EmailField()
    social_instagram = models.URLField(blank=True, null=True)
    social_telegram = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    logo_url = models.URLField(blank=True, null=True)
    chat_id = models.CharField(max_length=50, blank=True, null=True)
    lookfiles = models.JSONField(default=list)
    telegram_notification = models.TextField(blank=True, null=True)

class LookFile(models.Model):
    contact = models.ForeignKey(
        'Contact',
        on_delete=models.CASCADE,
        related_name='files'
    )
    file = models.FileField(upload_to='lookfiles/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.description or self.file.name
