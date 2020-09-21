from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name="homepage"),
    path('OwnerHome/<int:pk>/', views.ownerHomeView, name="home_list_owner"),
    path('myHome/<int:pk>/', views.myHomeView, name="home_list"),
    path('user/<int:pk>/', views.userProfileView, name="user_profile"),
    path('modify_user/<str:owner>/', views.ModifyProfileView, name="modify_profile"),
    path('thunder/', views.thunderCasa, name="thunder_casa"),
    path('search/', views.searchView, name="search_view"),
    path('underCostruction/', views.underCostructionView, name="under_costruction_view"),
    path('presentazione/', views.underCostructionPView, name="under_costruction_p_view"),
    path('about/', views.about, name="about_view"),



]
