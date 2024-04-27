from django.urls import path
from . import views

app_name = 'quality_control'

#Function-Based Views
urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
]

#Class-Based Views
# from django.urls import path
# from .views import IndexView, BugReportListView, BugReportDetailView, FeatureRequestListView, FeatureRequestDetailView
#
# app_name = 'quality_control'
#
# urlpatterns = [
#     path('', IndexView.as_view(), name='index'),
#     path('bugs/', BugReportListView.as_view(), name='bug_list'),
#     path(r'bugs/<int:bug_list_id>/', BugReportDetailView.as_view(), name='bug_detail'),
#     path('features/', FeatureRequestListView.as_view(), name='feature_list'),
#     path(r'features/<int:feature_request_id>/', FeatureRequestDetailView.as_view(), name='feature_detail'),
# ]

