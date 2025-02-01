
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Case, Evidence
from .forms import CaseForm, EvidenceForm

def home(request):
    total_cases = Case.objects.count()
    total_items = Evidence.objects.count()
    
    yearly_report = [
        (2023, 50, 100),  
        (2022, 30, 75),
        (2021, 20, 40),
    ]

    context = {
        'total_cases': total_cases,
        'total_items': total_items,
        'yearly_report': yearly_report,
    }
    
    return render(request, 'inventory/home.html', context)

def case_list(request):
    cases = Case.objects.annotate(item_count=Count('evidences'))  
    total_cases = cases.count()
    return render(request, 'inventory/case_list.html', {'cases': cases, 'total_cases': total_cases})


def case_detail(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    evidences = case.evidences.all()
    return render(request, 'inventory/case_detail.html', {'case': case, 'evidences': evidences})

def add_case(request):
    if request.method == "POST":
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save()  
            return redirect('case_detail', case_id=case.id)  
    else:
        form = CaseForm()  

    return render(request, 'inventory/add_case.html', {'form': form})

def edit_case(request, case_id):
    case = get_object_or_404(Case, id=case_id)  
    if request.method == "POST":
        form = CaseForm(request.POST, instance=case)  
        if form.is_valid():
            form.save() 
            return redirect('case_detail', case_id=case.id)  
    else:
        form = CaseForm(instance=case)  

    return render(request, 'inventory/edit_case.html', {'form': form, 'case': case})

def delete_case(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    if request.method == "POST":
        case.delete()
        return redirect('case_list')  
    return render(request, 'inventory/delete_case.html', {'case': case})

def evidence_list(request):
    search_query = request.GET.get('search', '')  # Get the search query from the request
    evidences = Evidence.objects.all()  # Get all evidence

    if search_query:
        evidences = evidences.filter(description__icontains=search_query)  # Filter by description

    total_evidence = evidences.count()
    
    return render(request, 'inventory/evidence_list.html', {
        'evidences': evidences,
        'total_evidence': total_evidence,
    })

def evidence_detail(request, evidence_id):
    evidence = get_object_or_404(Evidence, id=evidence_id)
    return render(request, 'inventory/evidence_detail.html', {'evidence': evidence})

def add_evidence(request, case_id=None):
    if case_id:
        case = get_object_or_404(Case, id=case_id)  
    else:
        case = None  

    if request.method == "POST":
        form = EvidenceForm(request.POST)
        if form.is_valid():
            evidence = form.save(commit=False)
            if case:
                evidence.case = case  
            evidence.save()
            return redirect('evidence_list')  
    else:
        form = EvidenceForm()

    return render(request, 'inventory/add_evidence.html', {
        'form': form,
        'case': case,
    })

def edit_evidence(request, evidence_id):
    evidence = get_object_or_404(Evidence, id=evidence_id)
    if request.method == "POST":
        form = EvidenceForm(request.POST, instance=evidence)
        if form.is_valid():
            form.save()
            return redirect('evidence_list')
    else:
        form = EvidenceForm(instance=evidence)

    return render(request, 'inventory/edit_evidence.html', {'form': form, 'evidence': evidence})

def delete_evidence(request, evidence_id):
    evidence = get_object_or_404(Evidence, id=evidence_id)
    if request.method == "POST":
        evidence.delete()
        return redirect('evidence_list')  
    return render(request, 'inventory/delete_evidence.html', {'evidence': evidence})

def reports(request):
    total_cases = Case.objects.count()
    total_items = Evidence.objects.count()
    
    # Example yearly report data
    yearly_report = [
        (2023, 50, 100),  # (Year, Total Cases, Total Items)
        (2022, 30, 75),
        (2021, 20, 40),
    ]

    context = {
        'total_cases': total_cases,
        'total_items': total_items,
        'yearly_report': yearly_report,
    }
    
    return render(request, 'inventory/reports.html', context)
