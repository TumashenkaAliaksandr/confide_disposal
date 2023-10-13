from django.shortcuts import render

def index(request):
    """Main, index constr"""

    return render(request, 'webapp/index.html')