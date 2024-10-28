from django.shortcuts import render,redirect,get_object_or_404
from .models import User,answer
import random

# Create your views here.
def start_q(request):
    return render(request, "start_q.html")
def end_exa(request):
    return render(request, "end.html")  

def insert(request):
    quest=request.POST['quest']
    A=request.POST['A']  
    Save=User(question=quest, A=A)
    Save.save()
    return redirect('add')

def show_quest(request):
    list_question=User.objects.all()
    return render(request, "add.html",{'question':list_question})

    


def add_tach(request, id):
    number_question=User.objects.get(id=id)
    return render(request, "add_answer.html",{'id':number_question})


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

def add_answer(request):
    if request.method == 'POST':
        id = request.POST.get('id')  
        option = request.POST.get('option')  
        answer = request.POST.get('answer')  
        try:
            
            add_question = User.objects.get(id=id)

            
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
    random_number = random.randint(1, 3)
    
    user = get_object_or_404(User, id=random_number)  # Fetch the user by ID

    # Create a dictionary to hold non-empty fields
    non_empty_fields = {}

    # Loop through all fields and check if they are not NULL or empty
    for field in user._meta.fields:
        value = getattr(user, field.name)  # Access the field value
        if value is not None and value != '':  # Check for non-empty value
            non_empty_fields[field.verbose_name] = value  # Use verbose_name for better readability

    return render(request, 'test.html', {'user': user, 'non_empty_fields': non_empty_fields,'random':user})
def save_answer(request):
    if answer.objects.count() <=20:
        
       question=request.POST['question']
       idq=request.POST['idq']
    
       answe=request.POST['answer']
       SaVe=answer(question=question,i=idq,true_A=answe)
       SaVe.save()
       return redirect('list')
       
    else:
        return redirect('add')
def end_delete(request):  # Accept the request parameter
    try:
        # Delete all entries in the Answer model
        answer.objects.all().delete()
        # Redirect to the start_q view after deletion
        return redirect('start_q')
    except Exception as e:
       pass
    
  
    