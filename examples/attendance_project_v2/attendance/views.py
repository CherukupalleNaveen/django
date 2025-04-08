from django.shortcuts import render, redirect
from .models import Student, Attendance

def student_list(request):
    students = Student.objects.all()
    return render(request, 'attendance/student_list.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        roll_number = request.POST['roll_number']
        Student.objects.create(name=name, roll_number=roll_number)
        return redirect('student_list')
    return render(request, 'attendance/add_student.html')

def mark_attendance(request):
    students = Student.objects.all()
    if request.method == "POST":
        for student in students:
            status = request.POST.get(f'status_{student.id}', 'Absent')
            Attendance.objects.create(student=student, status=status)
        return redirect('attendance_list')
    return render(request, 'attendance/mark_attendance.html', {'students': students})

def attendance_list(request):
    records = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {'records': records})
