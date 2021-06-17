from django import forms
from stnk.models import Opd, Asset



class TambahOpdForm(forms.ModelForm):
    class Meta:
        model  = Opd
        fields = '__all__'

class TambahAssetForm(forms.ModelForm):
    class Meta:
        model   = Asset
        fields  = '__all__'
        widgets = {
            'pajak': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'masa_aktif': forms.DateInput(attrs={'class':'form-control', 'type':'date'})
        } 
    
    def __init__(self, *args, **kwargs):
        super(TambahAssetForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class']='form-control-sm'

