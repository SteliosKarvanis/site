# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms

class LoginForm(forms.Form):
    fullName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "e.g: Stelios Karvanis",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "e.g: SecretP@ssword!",
                "class": "form-control"
            }
        ))
    siteDomain = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "e.g: twitter.com",
                "class": "form-control"
            }
        ))