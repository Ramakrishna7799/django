from django import forms
from django.forms import ModelForm
from .models import director, manager, engineer


class dform(ModelForm):
    class Meta:
        model = director
        fields = ['d_name']


class mform(ModelForm):
    class Meta:
        model = manager
        fields = ['m_name']


class eform(ModelForm):
    class Meta:
        model = engineer
        fields = ['e_name']
