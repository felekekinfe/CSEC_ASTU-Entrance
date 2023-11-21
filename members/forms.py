from django.contrib.auth.forms import AuthenticationForm
from django import forms
from CSEC_APP.models import Members

from django import forms

class MemberLoginForm(AuthenticationForm):
    idnumber=forms.CharField(max_length=20,required=True)

    def clean(self):
        cleaned_data=super().clean()

        idnumber=cleaned_data["idnumber"]
        password=cleaned_data["password"]

        if idnumber and password:
            member=Members.objects.filter(ID_Number=idnumber).first()
            if member and member.check_password(password):
                return cleaned_data


class EditMemberProfile(forms.ModelForm):
    class Meta:
        model=Members
        fields=['username','ID_Number','Roll','department','email','password1','password2']

      

            
            
        

        
