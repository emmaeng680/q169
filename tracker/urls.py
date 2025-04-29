from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('collection/<int:collection_id>/', views.collection_questions, name='collection_questions'),
    path('toggle_solved/<int:question_id>/', views.toggle_solved, name='toggle_solved'),
    path('increment_review/<int:question_id>/', views.increment_review, name='increment_review'),
    # Add these new URLs
    path('decrement_review/<int:question_id>/', views.decrement_review, name='decrement_review'),
    path('reset_review/<int:question_id>/', views.reset_review, name='reset_review'),
    # Add this URL pattern
    path('accounts/register/', views.register, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),
]