from django.contrib.auth.models import User
from django.shortcuts import render


def index(request):
    user = User.objects.prefetch_related(
        "portfolio", "portfolio__images", "testimonials"
    ).get(username="huzaifa")
    return render(request, "portfolio/index.html", {"user": user})
