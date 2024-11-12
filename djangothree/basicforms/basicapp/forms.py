from django import forms

# Fungsi cek 'a' sbg validasi
def check_for_a(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError("Name needs to start with A")

# Form validasi
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Input your email again")  # Add verify_email field
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()  # Get all cleaned data
        email = all_clean_data.get('email')  # Use .get() to avoid KeyError
        verify_email = all_clean_data.get('verify_email')  # Use .get() here as well
         
        if email and verify_email and email != verify_email:
            raise forms.ValidationError("Make sure emails match!")
    
        return all_clean_data  # Always return cleaned data
