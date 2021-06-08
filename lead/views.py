from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lead
from .forms import LeadForm
import datetime

@login_required
def show_view(request):
    leads = Lead.objects.filter(user=request.user, active=True)
    return render(request, 'lead/show.html', {'leads': leads})

@login_required
def archive_view(request):
    leads = Lead.objects.filter(user=request.user, active=False)
    return render(request, 'lead/archive.html', {'leads': leads})

@login_required
def create_view(request):
    if request.method == 'GET':
        return render(request, 'lead/create.html', {'form': LeadForm()})
    else:
        try:
            form = LeadForm(request.POST)
            newlead = form.save(commit=False)
            newlead.user = request.user
            newlead.save()
            return redirect('show-view')
        except ValueError:
            return render(request, 'lead/create.html', {'form': LeadForm(), 'error': 'Bad data. Try again'})

@login_required
def update_view(request, lead_pk):
    lead = get_object_or_404(Lead, pk=lead_pk, user=request.user)

    if request.method == 'GET':
        form = LeadForm(instance=lead)
        return render(request, 'lead/update.html', {'form': form})
    else:
        try:
            form = LeadForm(request.POST, instance=lead)
            form.save()
            return redirect('show-view')
        except ValueError:
            return render(request, 'lead/update.html', {'form': form, 'error': 'Bad data. Try again'})

@login_required
def archive_action_view(request, lead_pk):
    lead = get_object_or_404(Lead, pk=lead_pk, user=request.user)

    if request.method == 'POST':
        lead.active = False
        lead.end = datetime.datetime.now()
        lead.save()
        return redirect('show-view')

@login_required
def activate_action_view(request, lead_pk):
    lead = get_object_or_404(Lead, pk=lead_pk, user=request.user)

    if request.method == 'POST':
        lead.active = True
        lead.end = None
        lead.save()
        return redirect('archive-view')