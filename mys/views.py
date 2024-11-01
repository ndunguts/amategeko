from django.shortcuts import render,redirect,get_object_or_404
from .models import User,answer,useraccount
import random

# Create your views here.
def insertexam(request):
    if not request.session.get('login1', False):
            return redirect('login')
    
    return render(request, "insertE.html")
def start_q(request):
     if not request.session.get('login1', False):
            return redirect('login')
     
     return render(request, "start_q.html")
def end_exa(request):
    if not request.session.get('login1', False):
            return redirect('login')
    user_id = request.session.get('userid', None)    
    number_questin = answer.objects.filter(iduser=user_id).count()
    if number_questin == 19:
          amanota = answer.objects.filter(iduser=user_id, concluson="true").count()

          return render(request, "end.html", {'amanota': amanota}) 
    else:
          
 
        return redirect('list')
def insert(request):
    no=request.POST['no']
    quest=request.POST['quest']
    answer=request.POST['A']  
    Save=User(question=quest, no=no, A=answer)
    Save.save()
    return redirect('add')

def show_quest(request):
    
    list_question=User.objects.all()
    return render(request, "add.html",{'question':list_question})

    


def add_tach(request, no):
    number_question=User.objects.get(no=no)
    return render(request, "add_answer.html",{'id':number_question})


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

def add_answer(request):
    if request.method == 'POST':
        no = request.POST.get('id')  
        option = request.POST.get('option')  
        answer = request.POST.get('answer')  
        try:
            
            add_question = User.objects.get(no=no)

            
            if hasattr(add_question, option):  # Check if the field exists on the model
                setattr(add_question, option, answer)  # Set the field to the new value
                add_question.save()  # Save the changes to the database
                return redirect('add')  # Redirect to a success page
            else:
                return HttpResponse(f"Field '{option}' does not exist on User model", status=400)

        except User.DoesNotExist:
            # If the User with the given ID does not exist, return an error message
            return HttpResponse("User not found", status=404)

    # If the request method is not POST, render the form or return an error
    return render(request, 'add_answer.html')  # Make sure to create this template

    
def user_detail(request):
    if not request.session.get('login1', False):
            return redirect('login')
    random_number = random.randrange(1, 50)
    
    user = get_object_or_404(User, no=random_number)  # Fetch the user by ID

    # Create a dictionary to hold non-empty fields
    non_empty_fields = {}

    # Loop through all fields and check if they are not NULL or empty
    for field in user._meta.fields:
        value = getattr(user, field.name)  # Access the field value
        if value is not None and value != '':  # Check for non-empty value
            non_empty_fields[field.verbose_name] = value  # Use verbose_name for better readability

    return render(request, 'test.html', {'user': user, 'non_empty_fields': non_empty_fields,'random':user})
def save_answer(request):
    if not request.session.get('login1', False):
            return redirect('login')
    user_id = request.session.get('userid', None)
    if answer.objects.filter(iduser=user_id).count() <= 18:
       question=request.POST['question']
       noq=request.POST['no']
    
       true_answer=request.POST['true_answer']
       user_answer=request.POST['user_answer']
       if user_answer == true_answer:
          SaVe=answer(question=question,noq=noq,iduser=user_id, true_Answer=true_answer,user_Answer=user_answer,concluson="true")
          SaVe.save()
       else:
           SaVe=answer(question=question,noq=noq,iduser=user_id, true_Answer=true_answer,user_Answer=user_answer,concluson="false")
           SaVe.save()
              
          
       return redirect('list')
      
       
    else:
        return redirect('end')
def end_delete(request):  
    if not request.session.get('login1', False):
            return redirect('login')
   
    try:
       
        # Get user_id from session
        user_id = request.session.get('userid', None)
        
        # Delete entries in the Answer model where iduser matches user_id
        answer.objects.filter(iduser=user_id).delete()
        
        # Redirect to the start_q view after deletion
        return redirect('start_q')
    except Exception as e:
        # Optionally, log the error or handle it as needed
        pass
def sinup(request):
    if request.method== 'POST':
        username=request.POST['signup-username']
        password=request.POST['signup-password']
        email=request.POST['signup-email']
        saveuser=useraccount(username=username,password=password,email=email)
        saveuser.save()
        if saveuser:
            
          return redirect('login') 
def user_login(request):
    if not request.session.get('login1', False):
            
            return render(request, 'login.html')
    return redirect('start_q')
from django.shortcuts import redirect

def check_login(request):
    if request.method == 'POST':
        username = request.POST['login-username']
        password = request.POST['login-password']

        user_account = useraccount.objects.filter(username=username) 
        if user_account.exists(): 
            for user in user_account:
                if password == user.password:
                    # Set session variables
                    request.session['userid'] = user.id
                    request.session['login1'] = True
                    return redirect('start_q')
            else:
                # Password is incorrect
                return redirect('login')
        else:
            # User does not exist
            return redirect('login')
    return redirect('login')  # Redirect on GET requests

def out(request):
    if not request.session.get('login1', False):
            return redirect('login')
    user_id = request.session.get('userid', None)
        
        # Delete entries in the Answer model where iduser matches user_id
    answer.objects.filter(iduser=user_id).delete()
        
    request.session.flush()
   
  
   
    return redirect('login')

def correct(request):
    if not request.session.get('login1', False):
            return redirect('login')
    user_id = request.session.get('userid', None)    
    number_question = answer.objects.filter(iduser=user_id).count()
    if number_question== 19:
            
        amanota = answer.objects.filter(iduser=user_id, concluson="true").count()
        correct=answer.objects.filter(iduser=user_id)
        
    
    
        return render(request, 'correct.html',{'correct':correct,'amanota':amanota})

    return redirect('list')
  
    
