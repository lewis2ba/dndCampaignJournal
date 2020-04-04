from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:campaign_id>/', views.campaignDetail, name = 'campaignDetail'),
    path('<int:campaign_id>/sessions/', views.sessionsView, name = 'sessionsView'),
    path('<int:campaign_id>/sessions/<int:session_id>/', views.sessionDetail, name = 'sessionsDetail')
]
