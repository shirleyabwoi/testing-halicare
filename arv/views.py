from django.shortcuts import render, get_object_or_404
from .models import ARVAvailability

def arv_list(request):
    arvs = ARVAvailability.objects.select_related("center").all().order_by("-last_updated")
    return render(request, 'arv/arv_list.html', {'arvs': arvs})

def arv_detail(request, pk):
    arv = get_object_or_404(ARVAvailability, pk=pk)
    return render(request, 'arv/arv_detail.html', {'arv': arv})


