from django.http import HttpResponse

def index(request):
    html = f"<h1>Система контроля качества</h1>"
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
