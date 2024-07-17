from django import forms
from .models import Course

# class CourseForm(forms.Form):
    # title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=200)
    # description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # mentor = forms.IntegerField()
    # image = forms.ImageField()
    # price = forms.FloatField()
    # rating = forms.FloatField()

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'mentor', 'price', 'rating']

