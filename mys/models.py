from django.db import models

# Create your models here.

class User(models.Model):
    question=models.CharField(max_length=200)
    no=models.CharField(max_length=150)
    E=models.CharField(max_length=150)
    A=models.CharField(max_length=150)
    B=models.CharField(max_length=150)
    C=models.CharField(max_length=150)
    D=models.CharField(max_length=150)
    
   
    
    class Meta:
        db_table = "User"
class answer(models.Model):
    question=models.CharField(max_length=200)
    noq=models.CharField(max_length=150)
    iduser=models.CharField(max_length=150)
    true_Answer=models.CharField(max_length=150)
    user_Answer=models.CharField(max_length=150)
    concluson=models.CharField(max_length=150)
    def __str__(self):
        return self.noq  
    
    
    
    class Meta:
        db_table = "answer"  
class useraccount(models.Model):
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    email=models.EmailField(max_length=150 , default='')
    
    def __str__(self):
        return self.username  
    class Meta:
        db_table="useraccount"   
        
                 
        
    
