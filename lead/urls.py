from django.urls import path
from .views import show_view, archive_view, update_view, create_view, archive_action_view, activate_action_view

urlpatterns = [
    path('show/', show_view, name='show-view'),
    path('create/', create_view, name='create-view'),
    path('archive/', archive_view, name='archive-view'),
    path('<int:lead_pk>/', update_view, name='update-view'),
    path('<int:lead_pk>/archive_action/', archive_action_view, name='archive-action-view'),
    path('<int:lead_pk>/activate_action/', activate_action_view, name='activate-action-view'),
]
