from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import SchoolClass, Student


@login_required
def home(request):
    """Simple home page."""
    classes = SchoolClass.objects.filter(homeroom_teacher=request.user)
    return render(request, "tracker/home.html", {"classes": classes})


@login_required
def class_detail(request, class_id):
    school_class = get_object_or_404(SchoolClass, pk=class_id)
    if school_class.homeroom_teacher != request.user and not request.user.is_superuser:
        return render(request, "tracker/forbidden.html", status=403)
    students = school_class.students.all()
    return render(request, "tracker/class_detail.html", {"class": school_class, "students": students})


@login_required
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, "tracker/student_detail.html", {"student": student})
