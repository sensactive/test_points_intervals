from django import forms

from mainapp.models import Point, Interval, Comment


class PointUpdateForm(forms.ModelForm):

    class Meta:
        model = Point
        fields = '__all__'


class IntervalUpdateForm(forms.ModelForm):

    class Meta:
        model = Interval
        fields = '__all__'


class CommentUpdateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
