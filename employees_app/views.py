from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date


def employee_overview(request):

    # Aufgabe 1
    employees = Employee.objects.all()

    # Aufgabe 2
    high_salary_employees = Employee.objects.filter(
        salary__gt=3000
    )

    # Aufgabe 3
    high_earners_count = Employee.objects.filter(
        salary__gte=5000
    ).count()

    # Aufgabe 4
    sales_avg = Employee.objects.filter(
        department__name='Sales'
    ).aggregate(
        avg_salary=Avg('salary')
    )
    filtered_employees = Employee.objects.filter(
        hire_date__lt=date(2022,1, 1)
    ).exclude(
        department__name='HR'
    )
    # Daten an das HTML-Template übergeben
    context = {
        'employees': employees,
        'high_salary_employees': high_salary_employees,
        'high_earners_count': high_earners_count,
        'sales_avg': sales_avg,
        'filtered_employees': filtered_employees
    }

    return render(request, 'employee_list.html', context)
