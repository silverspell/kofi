from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^json/save/$', views.handle_post, name="post_handler"),
    url(r'^json/(?P<echovar>\w+)/$', views.echo_json, name='echo_test'),
    url(r'^json/$', views.test_json, name='json_test'),

]
