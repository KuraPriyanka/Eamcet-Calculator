from django.shortcuts import render
from .functions.result import process_link

# Create your views here.


def hello_world(request):
    if request.method == "POST":
        link = str(request.POST["link"])
        details = process_link(link)
        return render(
            request,
            "homeapp/result.html",
            {"total_score": details[5], "name": details[0], "hall_ticket_number": details[1], "maths_score": details[2], "physics_score": details[3], "chemistry_score": details[4]},
        )
    return render(request, "homeapp/hello.html")
