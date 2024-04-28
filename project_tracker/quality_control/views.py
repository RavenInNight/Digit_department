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
    feature = get_object_or_404(FeatureRequest, id=feature_id)
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

def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})

def update_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=feature.id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})

def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bug_list')

def delete_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect('quality_control:feature_list')





#Class-Based Views

# from django.views import View
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.shortcuts import render
# from .models import BugReport, FeatureRequest
# from .forms import BugReportForm, FeatureRequestForm
# from django.urls import reverse, reverse_lazy
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
#
# class BugCreateView(CreateView):
#     model = BugReport
#     form_class = BugReportForm
#     template_name = 'quality_control/bug_create.html'
#     success_url = reverse_lazy('quality_control/:projects_list')
#
# class FeatureCreateView(CreateView):
#     model = FeatureRequest
#     form_class = FeatureRequestForm
#     template_name = 'quality_control/feature_create.html'
#     success_url = reverse_lazy('quality_control/:feature_list')
#
# class BugUpdateView(UpdateView):
#     model = BugReport
#     form_class = BugReportForm
#     template_name = 'quality_control/bug_update.html'
#     pk_url_kwarg = 'bug_id'
#     success_url = reverse_lazy('quality_control:bug_list')
#
# class FeatureUpdateView(UpdateView):
#     model = FeatureRequest
#     form_class = FeatureRequestForm
#     template_name = 'quality_control/feature_update.html'
#     pk_url_kwarg = 'feature_id'
#     success_url = reverse_lazy('quality_control:feature_list')
#
# class BugDeleteView(DeleteView):
#     model = BugReport
#     pk_url_kwarg = 'bug_id'
#     success_url = reverse_lazy('quality_control:bug_list')
#     template_name = 'quality_control/bug_confirm_delete.html'
#
# class FeatureDeleteView(DeleteView):
#     model = FeatureRequest
#     pk_url_kwarg = 'feature_id'
#     success_url = reverse_lazy('quality_control:feature_list')
#     template_name = 'quality_control/feature_confirm_delete.html'




