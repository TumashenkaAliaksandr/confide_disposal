from django.shortcuts import render
from webapp.models import *



def index(request):
    """Main, index constr"""

    desposal = Disposal.objects.all()
    main_desposal = Disposal.objects.filter(is_main=True).first()

    context = {
        'desposal': desposal,
        'main_desposal': main_desposal,
    }
    return render(request, 'webapp/index.html', context=context)


def slider(request):
    """Slider, index constr"""

    slide = Slider.objects.all()
    main_slide = Disposal.objects.filter(is_main=True).first()

    context = {
        'slide': slide,
        'main_slide': main_slide,
    }
    return render(request, 'webapp/index.html', context=context)