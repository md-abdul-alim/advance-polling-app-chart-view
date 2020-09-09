from .import views
from django.urls import path
app_name = 'poll'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/results/', views.results, name='results'),
    path('<int:id>/vote/', views.vote, name='vote'),
    # path('resultdata/<int:id>/',views.resultsData, name="resultData")
    path('resultsdata/<str:id>/', views.resultsData, name="resultsdata")
]
