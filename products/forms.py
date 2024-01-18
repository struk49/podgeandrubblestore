from django import forms
from .models import Product, Category, Gender
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        gender = Gender.objects.all()
        categories = Category.objects.all() 
        gender_display_name = [(
            g.id,
            g.gender_display_name()
        )for g in gender]
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
        self.fields['gender'].choices = gender_display_name