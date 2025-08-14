from django.shortcuts import render, redirect, get_object_or_404
from .models import Lead
from .forms import LeadForm


# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')

# def leads_view(request):
#     return render(request, 'dashboard/leads.html')


# Read (List)
def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'dashboard/leads.html', {'leads': leads})

# Create
def lead_create(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead_list')
    else:
        form = LeadForm()
    return render(request, 'dashboard/lead_form.html', {'form': form, 'title': 'Add Lead'})

# Update
def lead_update(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('lead_list')
    else:
        form = LeadForm(instance=lead)
    return render(request, 'dashboard/lead_form.html', {'form': form, 'title': 'Edit Lead'})

# Delete
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        lead.delete()
        return redirect('lead_list')
    return render(request, 'dashboard/lead_confirm_delete.html', {'lead': lead})


