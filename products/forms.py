from django import forms
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


STAR_CHOICES = (
    (5, ""),
    (4, ""),
    (3, ""),
    (2, ""),
    (1, ""),
)


class ReviewForm(forms.ModelForm):
    """
    This Class is responsible for creating the form on the review section
    of the homepage.
    """

    rating = forms.ChoiceField(
        choices=STAR_CHOICES,
        widget=forms.RadioSelect(
            attrs={
                "class": "icon",
                "aria-label": "star-rating",
            }
        ),
    )

    class Meta:
        model = Review
        fields = ["rating", "comment"]
