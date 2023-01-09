from django.shortcuts import render

# from . import models
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    user = User.objects.prefetch_related("portfolio", "portfolio__images", "testimonials").get(
        username="huzaifa"
    )
    return render(request, "portfolio/index.html", {"user": user})
