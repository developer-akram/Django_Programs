from django.db import models

class Student(models.Model):
    roll = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    branch = models.CharField(max_length = 50)
    fees = models.IntegerField()
    
    def __str__(self):
        return f"Name : {self.name} Roll : {self.roll} Branch : {self.branch} Fees : {self.fees}"
        
