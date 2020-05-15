from django import forms, ModelForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'location']