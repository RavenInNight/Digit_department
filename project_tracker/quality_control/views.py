from django.shortcuts import render, get_object_or_404, redirect
from .models import BugReport, FeatureRequest
from .forms import BugReportForm, FeatureRequestForm
from django.urls import reverse

#Function-Based Views
def index(request):
    return render(request, 'quality_control/index.html')

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})

def feature_detail(request, feature_id):
    feature = get_object_or_404(BugReport, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})

def bug_report_create(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('quality_control:index'))
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def feature_request_create(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('quality_control:index'))
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})




#Class-Based Views

# from django.views import View
# from django.views.generic import ListView, DetailView
# from django.shortcuts import render
# from .models import BugReport, FeatureRequest
#
# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'quality_control/index.html')
#
# class BugReportListView(ListView):
#     model = BugReport
#     template_name = 'quality_control/bug_list.html'
#
# class FeatureRequestListView(ListView):
#     model = FeatureRequest
#     template_name = 'quality_control/feature_list.html'
#
# class BugReportDetailView(DetailView):
#     model = BugReport
#     pk_url_kwarg = 'bug_id'
#     template_name = 'quality_control/bug_detail.html'
#
# class FeatureRequestDetailView(DetailView):
#     model = FeatureRequest
#     pk_url_kwarg = 'feature_id'
#     template_name = 'quality_control/feature_detail.html'




