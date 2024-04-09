import openai
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        password2 = request.POST.get("pass2")
        

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("/signup")
        
        # Creating a user without validating inputs may lead to security vulnerabilities.
        try:
            # Use Django's built-in `create_user` method to handle password hashing.
            myuser = User.objects.create_user(username, email, password)
        except Exception as e:
            # Handle exceptions, such as a unique constraint violation for username or email.
            messages.error(request, f"Failed to create user: {e}")
            return redirect("/signup")
        
        messages.success(request, "Your account has been successfully created!")
        
        return redirect("/login")
    
    else:
        return render(request, "signup.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # Pass username as a context variable
            return render(request, "home.html", {"username": user.username})
        else:
            messages.error(request, "Bad credentials...")
            return redirect("login")  # Redirect to a named URL pattern

    else:
        return render(request, "login.html")


def ai(request):
    openai.api_key = "YOUR_OPENAI_API_KEY_HERE"
    if request.method == "POST":
        if 'message' in request.POST:
            user_message = request.POST['message']
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}]
            )
            full_response = response.choices[0].message.content.strip()

            return JsonResponse({'response': full_response})
        else:
            return JsonResponse({'error': 'Invalid request'})
    else:
        return render(request, "ai.html")
    
    

def user_logout(request):
    logout(request)
    messages.success(request, "Log out succesfully !")
    return redirect("/")



def catalog(request):
    return render(request, "catalog.html")


def collection(request):
    return render(request, "collection.html")