from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 50)
    email_id = models.EmailField(max_length = 50)
    roll_no = models.CharField(max_length = 6)
  

    def __str__(self):
        return self.name
