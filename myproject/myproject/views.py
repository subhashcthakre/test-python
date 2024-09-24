from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, World, you arrived at home page.")


def about(request):
    return HttpResponse("Hello, World, you arrived at About page.")


def contact(request):
    return HttpResponse("Hello, World, you arrived at Contact page.")

