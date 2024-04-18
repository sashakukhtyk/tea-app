from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
import openai
import random
from .models import Product


openai_api_key = "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"
openai.api_key = openai_api_key


def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer


# Create your views here.
def ai(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        return JsonResponse({'message': message, 'response': response})

    return render(request, 'ai.html')



def home(request):
    # Get all products from the database
    products = Product.objects.all()

    # Check if there are any products
    if products:
        # Select a random product from the queryset
        random_product = random.choice(products)

        # Pass the random product to the template
        return render(request, "home.html", {'random_product': random_product})
    else:
        # If there are no products, pass an empty context
        return render(request, "home.html", {})


def catalog(request):
    products = Product.objects.all()

    return render(request, "catalog.html", {'products' : products})


def product(request,pk):
    product = Product.objects.get(id=pk)

    return render(request, "product.html", {'product' : product})


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


def user_logout(request):
    logout(request)
    messages.success(request, "Log out succesfully !")
    return redirect("/")


@login_required
def collection_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user not in product.favourite.all():
        product.favourite.add(request.user)
        messages.success(request, "Product added successfully!")
        return redirect('my_collection')
    else:
        messages.error(request, "Product already in your collection.")
        return redirect(request.META.get('HTTP_REFERER'))


@login_required
def collection_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user in product.favourite.all():
        product.favourite.remove(request.user)
        messages.success(request, "Product removed successfully!")
        return redirect('my_collection')
    else:
        messages.error(request, "You are not authorized to remove this product.")
        return redirect('my_collection')


@login_required
def my_collection(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'collection_summary.html', context)