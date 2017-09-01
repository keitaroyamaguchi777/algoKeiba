from django.conf.urls import url
from sampling import views

urlpatterns = [
    # 書籍
    url(r'^umakihon/$', views.uma_kihon_list, name='uma_kihon_list'),   # 一覧
    url(r'^umakihon/add/$', views.uma_kihon_edit, name='uma_kihon_add'),  # 登録
    url(r'^umakihon/mod/(?P<uma_kihon_id>\d+)/$', views.uma_kihon_edit, name='uma_kihon_mod'),  # 修正
    url(r'^umakihon/del/(?P<uma_kihon_id>\d+)/$', views.uma_kihon_del, name='uma_kihon_del'),   # 削除
]
