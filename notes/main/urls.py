from django.urls import path, include

from main import views

urlpatterns = [

    path('', views.Index.as_view(), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.UserCreating.as_view(), name='register'),
    path('add_note/', views.add_note, name='add_note'),
    path('remove/', views.remove, name='remove')
]
