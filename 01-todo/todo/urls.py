from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.TodoListView.as_view(), name='list'),
    path('add/', views.TodoCreateView.as_view(), name='add'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.TodoUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='delete'),
    path('<int:pk>/toggle/', views.toggle_complete, name='toggle_complete'),
]