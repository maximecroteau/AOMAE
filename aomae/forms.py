from django import forms

from .models import Contact


class AddToCartForm(forms.Form):
    product_id = forms.IntegerField(required=True)
    product_size = forms.CharField(max_length=20)
    product_color = forms.CharField(max_length=20)

    class Meta:
        fields = ('product_id', 'product_color')


class RemFromCartForm(forms.Form):
    toRem = forms.CharField(max_length=100)

    class Meta:
        fields = ('toRem',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'name', 'mail', 'subject', 'message']
