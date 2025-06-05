from django.urls import path
from .views import discussion_list, add_reply

urlpatterns = [
    path('discussions/', discussion_list, name='discussion-list'),
    path('discussions/<int:discussion_id>/reply/', add_reply, name='add-reply'),
]
