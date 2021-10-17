from django import forms


class DocumentUploadForm(forms.Form):

    description = forms.CharField(
        max_length=100,
        help_text='Optional description for the uploaded document.',
        required=False
    )
    document = forms.FileField(
        label='Select a file'
    )
