# Create your views here.
from django.shortcuts import render
import csv
import sqlite3
from django.http import HttpResponse
from .models import Student

def export_csv(request):
    template_name = 'Posts/main.html'
    # Create a CSV response object
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exportDataset.csv"'

    students = Student.objects.all()

    # Create a CSV writer object
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(['FirstName', 'LastName', 'City'])

    # Write the data rows
    for row in students:
        writer.writerow(row)

    return response
   



