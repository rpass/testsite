from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^netflow', views.netflow, name='netflow'),
    url(r'^mycf', views.mycrossfilter, name='mycrossfilter'),
    url(r'^mydcseries', views.mydcseries, name='mydcseries'),
    url(r'^dcseries', views.dcseries, name='dcseries'),
    url(r'^chordexample$', views.chord_example, name='chord_example'),
    url(r'^chord$', views.chord, name='chord'),
    url(r'^team$', views.team, name='team'),
    url(r'^sigma$', views.sigmaexample, name='sigma'),
    url(r'^arctic$', views.arcticexample, name='arctic'),
    url(r'^crossfilter$', views.crossFilterExample, name='crossfilter'),
    url(r'^demo$', views.demoExamples, name='demo'),
    url(r'^igraph$', views.igraphExample, name='igraph'),
    url(r'^data/(?P<file>.+)$', views.fetchdata, name='fetchdata'),
    url(r'^d3tut/(?P<part>.+)$', views.d3tut, name='d3tut'),
    url(r'^jq$', views.jq, name='jq'),
    url(r'^(?P<id>[0-9]+)/vote$', views.vote, name='vote'),
    url(r'^vote$', views.votepage, name='votepage'),
    url(r'.+', views.http404, name='404'),
]
