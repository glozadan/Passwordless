from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.AccountsView.as_view()),
    path('<int:id>', views.AccountsSingleView.as_view()),
]