from django.urls import path
from django.views.generic import TemplateView
from .views import ProfileView, ProfileCreate, ProfileEdit, ProfileDelete


urlpatterns = [
    path('', ProfileView.as_view(),name='home'),
    path('edit/<uuid:pk>/', ProfileEdit.as_view(), name='edit'),
    path('create/', ProfileCreate.as_view(), name="new"),
    path('delete/<uuid:pk>/', ProfileDelete.as_view(), name='delete')
]