from django.urls  import path
from app import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login_view/',v.login_view),
    path('list',v.post_list),
    path('edit',v.post_edit),
    path('dashboard/',v.dashboard),
    path('create',v.create_post),
    path('login/',v.login),
    path('',v.signup),
]
