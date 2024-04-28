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
    path('bug_form/', views.bug_report_create, name='bug_report_create'),
    path('feature_from/', views.feature_request_create, name='feature_request_create'),
    path('bugs/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    path('features/<int:feature_id>/update/', views.update_feature, name='update_feature'),
    path('bugs/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.delete_feature, name='delete_feature'),
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
#     path('bugs/<int:bug_id>/', BugReportDetailView.as_view(), name='bug_detail'),
#     path('features/', FeatureRequestListView.as_view(), name='feature_list'),
#     path('features/<int:feature_id>/', FeatureRequestDetailView.as_view(), name='feature_detail'),
#     path('bugs/create/', views.BugCreateView.as_view(), name='bug_create'),
#     path('features/create/', views.FeatureCreateView.as_view(), name='feature_create'),
#     path('bugs/<int:bug_id>/update/', views.BugUpdateView.as_view(), name='bug_update'),
#     path('features/<int:feature_id>/update/', views.FeatureUpdateView.as_view(), name='feature_update'),
#     path('bugs/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='bug_delete'),
#     path('features/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='feature_delete'),
# ]

