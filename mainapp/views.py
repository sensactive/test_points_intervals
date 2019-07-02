from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from mainapp.forms import PointUpdateForm, IntervalUpdateForm, CommentUpdateForm
from mainapp.models import Point, Interval, Comment


def main_view(request):
    return render(request, 'mainapp/index.html')


class PointsListView(ListView):
    model = Point
    queryset = Point.objects.order_by('pk')
    template_name = 'mainapp/points.html'
    context_object_name = 'points'
    paginate_by = 20


class PointCreateView(CreateView):
    model = Point
    template_name = 'mainapp/point_create.html'
    form_class = PointUpdateForm
    success_url = reverse_lazy('mainapp:points')


class PointUpdateView(UpdateView):
    model = Point
    form_class = PointUpdateForm
    template_name = 'mainapp/point_update.html'
    success_url = reverse_lazy('mainapp:points')


class PointDeleteView(DeleteView):
    model = Point
    template_name = 'mainapp/point_delete.html'
    success_url = reverse_lazy('mainapp:points')


class IntervalsListView(ListView):
    model = Interval
    queryset = Interval.objects.order_by('pk')
    template_name = 'mainapp/intervals.html'
    context_object_name = 'intervals'
    paginate_by = 20


class IntervalCreateView(CreateView):
    model = Interval
    template_name = 'mainapp/interval_create.html'
    form_class = IntervalUpdateForm
    success_url = reverse_lazy('mainapp:intervals')


class IntervalUpdateView(UpdateView):
    model = Interval
    form_class = IntervalUpdateForm
    template_name = 'mainapp/interval_update.html'
    success_url = reverse_lazy('mainapp:intervals')


class IntervalDeleteView(DeleteView):
    model = Interval
    template_name = 'mainapp/interval_delete.html'
    success_url = reverse_lazy('mainapp:intervals')


class CommentsListView(ListView):
    model = Comment
    queryset = Comment.objects.order_by('pk')
    template_name = 'mainapp/comments.html'
    context_object_name = 'comments'
    paginate_by = 20


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'mainapp/comment_create.html'
    form_class = CommentUpdateForm
    success_url = reverse_lazy('mainapp:comments')


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentUpdateForm
    template_name = 'mainapp/comment_update.html'
    success_url = reverse_lazy('mainapp:comments')


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'mainapp/comment_delete.html'
    success_url = reverse_lazy('mainapp:comments')
