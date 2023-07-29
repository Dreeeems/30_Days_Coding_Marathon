from django.db import models

# Create your models here.


class Todos(models.Model):
    todo_name = models.CharField(max_length=150)
    todo_desc = models.CharField(max_length=200, default=0)
    todo_status = models.BooleanField(default=False)
     
    def __str__(self):
       return f' Todo:  {self.todo_name} {self.todo_desc}'