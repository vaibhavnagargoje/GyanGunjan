from django.shortcuts import render, redirect

# Create your views here.

from .models import Contribute

def Contribute_view(request):

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        subscribed = request.POST.get("subscribed") == "on"
        message = request.POST.get("message")
        photo = request.FILES.get("photo")
        video = request.FILES.get("video")
        pdf = request.FILES.get("pdf")

        Contribute.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            subscribed=subscribed,
            message=message,
            photo=photo,
            video=video,
            pdf=pdf,
        )
        return redirect("success_page")  # Replace with your success page URL

    contributors = Contribute.objects.all()
    return render(request,"contribute/contribute.html",{"contributors": contributors})
