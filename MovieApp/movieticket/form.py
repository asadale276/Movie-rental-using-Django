from django import forms
from .models import User

class std(forms.ModelForm):
    class Meta:
        model = User
        fields = ('std_name', 'std_contact', 'std_address', 'movie')
        labels = {
            'std_name' : 'Name',
            'std_contact' : 'Contact',
            'std_address' : 'Address'
        }
    def __init__(self, *args, **kwargs):
        super(std, self).__init__(*args, **kwargs)
        self.fields['movie'].empty_label = "Select"
