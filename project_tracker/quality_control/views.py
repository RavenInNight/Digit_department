from django.http import HttpResponse
from django.urls import reverse

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
