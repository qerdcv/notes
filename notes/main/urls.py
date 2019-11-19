from django.urls import path, include

from main import views

urlpatterns = [

    path('', views.Index.as_view(), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.UserCreating.as_view(), name='register'),
    path('add_note/', views.AddNote.as_view(), name='add_note'),
    path('remove/', views.RemoveNote.as_view(), name='remove')
]
