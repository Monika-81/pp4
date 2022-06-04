from django.urls import path
from . import views


urlpatterns = [
    path('', views.TopicList.as_view(), name='home'),
    path('topic/<str:topic>', views.TopicDisplay.as_view(),
         name='topic_display'),
    path('add-post', views.AddPost.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDisplay.as_view(), name="post_display"),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post', views.AddPost.as_view(), name='add_post'),
    path('edit_post/<slug:slug>', views.EditPost.as_view(), name='edit_post'),
]
