from django.db import models

class employees(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    employeeId=models.IntegerField()

    def __str__(self):
        return self.firstName
