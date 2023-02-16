from django import forms
from django.core import validators
from first_app.models import Accessrecord

# #custom function
# def checkz(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAMES NEED TO START WITH Z")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean = super().clean()
        email = all_clean['email']
        vmail = all_clean['verify_email']
        if email != vmail:
            raise forms.ValidationError("MAKE SURE BOTH EMAILS ARE CORRECT")

    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    # #checking for bots
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher


