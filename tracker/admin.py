from django.contrib import admin

from .models import SchoolClass, Student, OrientationRecord, Note


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "homeroom_teacher")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "school_class")
    search_fields = ("last_name", "first_name")


@admin.register(OrientationRecord)
class OrientationRecordAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "year",
        "trimester",
        "orientation_type",
        "created_at",
    )
    list_filter = ("year", "orientation_type")


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("student", "author", "created_at")
    search_fields = ("text",)
