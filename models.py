from django.db import models


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    year_level = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Equipment(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Borrowed', 'Borrowed'),
        ('Under Maintenance', 'Under Maintenance'),
    ]
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return self.name


class BorrowRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Borrowed', 'Borrowed'),
        ('Returned', 'Returned'),
    ]
    borrower = models.ForeignKey(Student, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date_needed = models.DateField()
    due_date = models.DateField()
    purpose = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    reason = models.TextField(blank=True, null=True)
    is_overdue = models.BooleanField(default=False)
    return_date = models.DateField(blank=True, null=True)
    is_damaged = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.borrower} - {self.equipment} ({self.status})"