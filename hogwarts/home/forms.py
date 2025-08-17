from django import forms

class ResultUploadForm(forms.Form):
    file = forms.FileField(
        label="Upload Excel File",
        help_text="Only .xlsx files are allowed",
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control",
            "accept": ".xlsx"
        })
    )


from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(
        label="Select Excel File (.xlsx)",
        widget=forms.ClearableFileInput(attrs={"accept": ".xlsx"})
    )
