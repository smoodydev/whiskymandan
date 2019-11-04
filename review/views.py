from django.shortcuts import render, get_object_or_404
from .models import Review

# Create your views here.
def get_review(request, pk):
    review = get_object_or_404(Review, id=pk)
    return render(request, "review.html", {"review": review})