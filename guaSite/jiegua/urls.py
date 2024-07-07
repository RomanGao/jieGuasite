from django.urls import path

from . import views

#设置命名空间
app_name ="dinggua"
urlpatterns = [
    #该path()函数传递四个参数，其中两个是必需的： route和view，两个可选的：kwargs, 和name

    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("detail/", views.detail, name="detail"),
    # ex: /polls/5/results/
    #path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    #path("<int:question_id>/vote/", views.vote, name="vote"),
]

'''
当有人从您的网站请求页面时 – 例如“/polls/34/”，Django 将加载mysite.urlsPython 模块，
因为它是由设置指向的 ROOT_URLCONF。它找到名为的变量urlpatterns 并按顺序遍历模式。
在 找到匹配项后'polls/'，它会去掉匹配文本 ( "polls/") 并将剩余文本发送 "34/"到 'polls.urls' URLconf 进行进一步处理。
在那里它匹配'<int:question_id>/'，导致对视图的调用，
'''