from django import forms
from events.models import Event, Participant, Category


class StyleFormMixin:
    default_classes = (
        "border-2 border-gray-300 p-2 rounded-lg shadow-sm focus:border-green-400"
    )

    def apply_style_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update(
                    {
                        "class": f"{self.default_classes} w-full",
                        "placeholder": f"Enter {field.label.lower()}...",
                    }
                )
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update(
                    {
                        "class": f"{self.default_classes} w-full bg-gray-50",
                        "placeholder": f"Enter {field.label.lower()}...",
                        "rows": 4,
                    }
                )
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update(
                    {
                        "class": "form-select",
                    }
                )


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_style_widgets()


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = "__all__"

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # if Participant.objects.filter(email=email).exists():
            # raise ValidationError("This email is already registered.")
        # return email


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
