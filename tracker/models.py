from django.db import models
from django.contrib.auth import get_user_model


class SchoolClass(models.Model):
    """Represents a class like 'Seconde A' or 'Premiere B'."""

    YEAR_CHOICES = [
        ("2nde", "Seconde"),
        ("1ere", "Premiere"),
        ("Tle", "Terminale"),
    ]

    name = models.CharField(max_length=20)
    year = models.CharField(max_length=5, choices=YEAR_CHOICES)
    homeroom_teacher = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.name} ({self.get_year_display()})"


class Student(models.Model):
    """Basic student information."""

    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    school_class = models.ForeignKey(
        SchoolClass, related_name="students", on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"


class OrientationRecord(models.Model):
    """Stores orientation choices or preferences for a given trimester."""

    ORIENTATION_TYPES = [
        ("preference", "Preference"),
        ("official", "Official"),
    ]

    student = models.ForeignKey(Student, related_name="orientations", on_delete=models.CASCADE)
    year = models.CharField(max_length=5, choices=SchoolClass.YEAR_CHOICES)
    trimester = models.PositiveSmallIntegerField()
    orientation_type = models.CharField(max_length=10, choices=ORIENTATION_TYPES)
    content = models.TextField(help_text="Orientation choice or preference")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return f"{self.student} - T{self.trimester} {self.get_year_display()}"


class Note(models.Model):
    """General notes or incidents about a student."""

    student = models.ForeignKey(Student, related_name="notes", on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Note for {self.student} on {self.created_at:%Y-%m-%d}"
