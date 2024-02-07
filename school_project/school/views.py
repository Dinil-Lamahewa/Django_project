import csv
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'index.html', context)

def import_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        file_reader = csv.reader(csv_file.file, delimiter=',')

        for row in file_reader:
            # Process the CSV file and create or update the records
            # For example, to create a new Student record:
            school = School.objects.get_or_create(name=row['school_name'])[0]
            class_name = Class.objects.get_or_create(name=row['class_name'])[0]
            assessment_area = AssessmentArea.objects.get_or_create(name=row['assessment_area'])[0]
            student, created = Student.objects.get_or_create(
                fullname=row['fullname'],
                defaults={
                    'class': class_name,
                }
            )
            Answer.objects.get_or_create(
                summary=row['answer_summary'],
                student=student,
            )

        return render(request, 'import_success.html')
    else:
        return render(request, 'import.html')
    from django.shortcuts import render

def import_data_view(request):
    # Your view logic here
    return render(request, 'import_data.html')