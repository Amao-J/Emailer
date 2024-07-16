from django import forms

class EmailForm(forms.Form):
    recipient = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Recipient Emails (separate with commas for multiple)")
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Subject")
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), label="Message")
    attachment = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}), required=False, label="Attachment")