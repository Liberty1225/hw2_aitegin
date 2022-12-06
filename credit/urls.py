from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClientView.as_view(), name='index'),
    path('<int:id>/detail/', views.ClientDetailView.as_view(template_name='detail.html'), name='detail'),
    # path('<int:id>/result/', views.ClientDetailView.as_view(template_name='result.html'), name='result'),
    # path('<int:id>/vote/', views.vote, name='vote'),

]