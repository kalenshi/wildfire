from django.shortcuts import render


def about(request) -> None:
    """
    View function for the about page
    """
    return render(request, "core/about.html", {})
