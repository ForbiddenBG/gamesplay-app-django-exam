from django.urls import path

from WebExam5.Profile.views import home_page, create_profile, dashboard_page, details_profile, edit_profile, \
    delete_profile

urlpatterns = (
    path('', home_page, name='index'),
    path('profile/create/', create_profile, name='create-profile'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('profile/details/', details_profile, name='details-profile'),
    path('profile/edit/', edit_profile, name='edit-profile'),
    path('profile/delete/', delete_profile, name='delete-profile'),
)
