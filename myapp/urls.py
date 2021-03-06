from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('getuserfeedbackform',views.getuserfeedbackform,name="getuserfeedbackform"),
    path('saveuserfeedbackform',views.saveuserfeedbackform,name="saveuserfeedbackform"),
    path('api',views.api,name='api'),
    path('search',views.search,name="search"),
    path('result',views.result,name='result'),
    path('about',views.about,name='about'),
    path('geturlhistory',views.geturlhistory,name="geturlhistory"),
    path('discuss',views.discuss,name="discuss"),
    path('reply/<int:replyid>',views.replyform,name="reply"),
    path('savereply',views.savereply,name="reply"),
    path('searchdiscuss',views.searchdiscuss,name="searchdiscuss"),
    path('getdataset',views.getdataset,name='getdataset'),
    path('getdocs',views.getdoc,name='namedoc'),
    path('updatee_view',views.updatee_view,name="updatee_view"),
    path('de_view',views.de_view,name="de_view"),
    path('showblack',views.showblack,name="showblack"),
    path('addcourse',views.addcourse,name="addcourse"),

]

