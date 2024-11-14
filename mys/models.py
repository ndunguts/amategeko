from django.db import models

# Create your models here.

class User(models.Model):
    question=models.CharField(max_length=500)
    no=models.CharField(max_length=500)
    E=models.CharField(max_length=500)
    A=models.CharField(max_length=500)
    B=models.CharField(max_length=500)
    C=models.CharField(max_length=500)
    D=models.CharField(max_length=500)
    
   
    
    class Meta:
        db_table = "User"
class answer(models.Model):
    question=models.CharField(max_length=500)
    noq=models.CharField(max_length=500)
    iduser=models.CharField(max_length=500)
    true_Answer=models.CharField(max_length=500)
    user_Answer=models.CharField(max_length=500)
    concluson=models.CharField(max_length=500)
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
        
                 
        
    
