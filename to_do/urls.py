"""to_do URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import TodoListView, TodoCreateView, TodoDetailView, TodoUpdateView, TodoDeleteView, DoneListView, NotDoneListView

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TodoListView.as_view(), name='list'),
    path('create', TodoCreateView.as_view(), name='create'),
    path('<int:pk>', TodoDetailView.as_view(), name='detail'),
    path('<int:pk>/update', TodoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', TodoDeleteView.as_view(), name='delete'),
    path('done', DoneListView.as_view(), name='done'),
    path('notdone', NotDoneListView.as_view(), name='notdone'),

    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
