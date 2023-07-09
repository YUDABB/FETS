from django import forms

class UploadFileForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=50)
    fileinput = forms.FileField()
    key = forms.CharField(max_length=32)