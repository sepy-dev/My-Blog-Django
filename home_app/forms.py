from django import forms

from django import forms
from django.core.validators import MinLengthValidator

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="نام کامل",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام کامل'
        }),
        validators=[MinLengthValidator(3, "نام باید حداقل ۳ کاراکتر باشد")]
    )
    
    email = forms.EmailField(
        label="آدرس ایمیل",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'آدرس ایمیل'
        })
    )
    
    text = forms.CharField(
        label="متن پیام",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'متن پیام'
        }),
        max_length=500,
        error_messages={
            'required': 'لطفا متن پیام را وارد کنید',
            'max_length': 'پیام شما نمی‌تواند بیشتر از ۵۰۰ کاراکتر باشد'
        }
    )