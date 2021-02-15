from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('stiri/<str:category>', views.post_list_category, name='post_list_category'),
    path('post/<int:pk>', views.post_item, name='post_item'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
    path('profile_page/<str:username>', views.profile_page, name='profile_page'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('delete_profile_image/', views.delete_profile_image, name='delete_profile_image'),
    path('viewed_profile/<str:comment_author>', views.viewed_profile, name='viewed_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
