from django import forms


class AddToCartForm(forms.Form):
    product_id = forms.IntegerField(required=True)
    product_size = forms.CharField(max_length=20)
    product_color = forms.CharField(max_length=20)

    class Meta:
        fields = ('product_id', 'product_color')
