# Create your views here.
import re
from django.shortcuts import render

def login_page(request):
    message = ""
    errors = []

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        if not re.fullmatch(r"[A-Za-z0-9]{3,}", username):
            errors.append("Username must contain at least 3 letters or numbers.")

        if not re.fullmatch(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            email
        ):
            errors.append("Enter a valid email address.")

        if not re.fullmatch(
            r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9])\S{8,}",
            password
        ):
            errors.append(
                "Password needs 8 characters, uppercase, lowercase, "
                "number and special character."
            )

        if errors:
            message = "Please correct the errors."
        else:
            message = "All fields are valid! Login form submitted."

    return render(
        request,
        "loginapp/login.html",
        {"message": message, "errors": errors}
    )