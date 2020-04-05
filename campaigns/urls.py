from django.urls import path

from . import views

app_name = 'campaigns'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:campaign_id>/', views.campaignDetail, name = 'campaignDetail'),
    path('<int:campaign_id>/sessions/<int:session_id>/', views.sessionDetail, name = 'sessionDetail'),
    path('<int:campaign_id>/sessions/new/', views.sessionNew, name='sessionNew')
]
