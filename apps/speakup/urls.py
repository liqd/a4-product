from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'create/module/(?P<module_slug>[-\w_]+)/$',
        views.SpeakupIdeaCreateView.as_view(), name='speakup-create'),
    url(r'^(?P<slug>[-\w_]+)/edit/$',
        views.SpeakupIdeaUpdateView.as_view(), name='speakup-update'),
    url(r'^(?P<slug>[-\w_]+)/delete/$',
        views.SpeakupIdeaDeleteView.as_view(), name='speakup-delete'),
    url(r'^(?P<slug>[-\w_]+)/$',
        views.SpeakupIdeaDetailView.as_view(), name='speakup-detail'),
]
