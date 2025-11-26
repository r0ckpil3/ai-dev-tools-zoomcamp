from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Home page (named 'home') — renders app's home template
    path('home/', TemplateView.as_view(template_name='todo/home.html'), name='home'),
    path('', include('todo.urls')),  # include todo app routes
    path('admin/', admin.site.urls),
]