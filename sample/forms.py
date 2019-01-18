from django import forms
from .models import *




class TicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields='__all__'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['age'].widget.attrs.update({'class':'form-control'})
        self.fields['gender'].widget.attrs.update({'class':'form-control','placeholder':'male/female'})
        self.fields['coach_name'].widget.attrs.update({'class':'form-control','placeholder':'Available S1 S2 S3 S4'})
        self.fields['upper'].widget.attrs.update({'class':'form-control','value':0,'min':0,'max':2})
        self.fields['lower'].widget.attrs.update({'class':'form-control','value':0,'min':0,'max':2})
        self.fields['middle'].widget.attrs.update({'class':'form-control','value':0,'min':0,'max':2})
        self.fields['side'].widget.attrs.update({'class':'form-control','value':0,'min':0,'max':2})

class Children(forms.Form):
    children=forms.BooleanField()