from django.http import HttpResponse
from django.urls import reverse

#Function-Based Views
def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1>" \
           f"<a href='{bug_list_url}'>Список всех багов</a>" \
           f"<br/><a href='{feature_list_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)

def bug_list(request):
    html = f"<h1>Cписок отчетов об ошибках</h1>"
    return HttpResponse(html)

def feature_list(request):
    html = f"<h1>Список запросов на улучшение</h1>"
    return HttpResponse(html)

def bug_detail(request, bug_id):
    html = f"<h1>Детали бага {bug_id}</h1>"
    return HttpResponse(html)

def feature_detail(request, feature_id):
    html = f"<h1>Детали улучшения {feature_id}</h1>"
    return HttpResponse(html)


#Class-Based Views

# from django.views import View
# from django.http import HttpResponse
# from django.views.generic import ListView, DetailView
# from .models import BugReport, FeatureRequest
# from django.urls import reverse
#
# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         bug_list_url = reverse('quality_control:bug_list')
#         feature_list_url = reverse('quality_control:feature_list')
#         html = f"<h1>Система контроля качества</h1>" \
#                f"<a href='{bug_list_url}'>Список всех багов</a>" \
#                f"<br/><a href='{feature_list_url}'>Запросы на улучшение</a>"
#         return HttpResponse(html)
#
# class BugReportListView(ListView):
#     model = BugReport
#
#     def get(self, request, *args, **kwargs):
#         bug_report = self.get_queryset()
#         bug_report_html = '<h1>Cписок отчетов об ошибках</h1><ul>'
#         for bug in bug_report:
#             bug_report_html += f'<li><a href="{bug.id}/">Ошибка {bug.id}</a></li>'
#         bug_report_html += '</ul>'
#         return HttpResponse(bug_report_html)
#
# class FeatureRequestListView(ListView):
#     model = FeatureRequest
#
#     def get(self, request, *args, **kwargs):
#         feature_request = self.get_queryset()
#         feature_request_html = '<h1>Список запросов на улучшение</h1><ul>'
#         for feature in feature_request:
#             feature_request_html += f'<li><a href="{feature.id}/">Запрос на улучшение {feature.id}</a></li>'
#         feature_request_html += '</ul>'
#         return HttpResponse(feature_request_html)
#
# class BugReportDetailView(DetailView):
#     model = BugReport
#     pk_url_kwarg = 'bug_list_id'
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         bug_report = self.object
#         response_html = f'<h1>Детали бага {bug_report.id}</h1><p>{bug_report.description}</p>'
#         return HttpResponse(response_html)
#
# class FeatureRequestDetailView(DetailView):
#     model = FeatureRequest
#     pk_url_kwarg = 'feature_request_id'
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         feature_request = self.object
#         response_html = f'<h1>Детали запроса на улучшение {feature_request.id}</h1><p>{feature_request.description}</p>'
#         return HttpResponse(response_html)




