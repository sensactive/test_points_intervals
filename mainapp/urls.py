from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'


urlpatterns = [
    path('', mainapp.main_view, name='main'),
    path('points/', mainapp.PointsListView.as_view(), name='points'),
    path('points/create/', mainapp.PointCreateView.as_view(), name='create_point'),
    path('points/<pk>/', mainapp.PointUpdateView.as_view(), name='update_point'),
    path('points/delete/<pk>/', mainapp.PointDeleteView.as_view(), name='delete_point'),
    path('intervals/', mainapp.IntervalsListView.as_view(), name='intervals'),
    path('intervals/create/', mainapp.IntervalCreateView.as_view(), name='create_interval'),
    path('intervals/<pk>/', mainapp.IntervalUpdateView.as_view(), name='update_interval'),
    path('intervals/delete/<pk>/', mainapp.IntervalDeleteView.as_view(), name='delete_interval'),
    path('comments/', mainapp.CommentsListView.as_view(), name='comments'),
    path('comments/create/', mainapp.CommentCreateView.as_view(), name='create_comment'),
    path('comments/<pk>/', mainapp.CommentUpdateView.as_view(), name='update_comment'),
    path('comments/delete/<pk>/', mainapp.CommentDeleteView.as_view(), name='delete_comment'),
]
