from django.contrib import admin
from .models import StudyApplication, JobApplication, Contact,  LookFile


@admin.register(StudyApplication)
class StudyApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'created_at')
    search_fields = ('full_name', 'email', 'phone')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'desired_position', 'expected_salary', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'desired_position')
    list_filter = ('created_at', 'desired_position')
    ordering = ('-created_at',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'social_instagram', 'social_telegram', 'address')
    search_fields = ('email', 'phone', 'address')


class LookFileInline(admin.TabularInline):
    model = LookFile
    extra = 1



