from django.db import models

# Create your models here.

class User(models.Model):
    question=models.CharField(max_length=200)
    A=models.CharField(max_length=30)
    B=models.CharField(max_length=30)
    C=models.CharField(max_length=30)
    D=models.CharField(max_length=30)
    E=models.CharField(max_length=30)
    F=models.CharField(max_length=30)
    
    class Meta:
        db_table = "User"
class answer(models.Model):
    question=models.CharField(max_length=200)
    idq=models.CharField(max_length=30)
    iduser=models.CharField(max_length=30)
    true_A=models.CharField(max_length=30)
    
    
    class Meta:
        db_table = "answer"  
class useraccount(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=10)
    email=models.EmailField(max_length=100 , default='')
    
    def __str__(self):
        return self.username  
    class Meta:
        db_table="useraccount"            
        
    