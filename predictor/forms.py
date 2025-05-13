from django import forms
class PlantInputForm(forms.Form):
    plant_name = forms.CharField(label="Plant Name", max_length=100)
    temperature = forms.IntegerField(label="Temperature")
    sunlight = forms.ChoiceField(choices=[])
    soil = forms.ChoiceField(choices=[])
    humidity = forms.IntegerField(label="Humidity")

    def __init__(self, *args, **kwargs):
        sunlight_choices = kwargs.pop('sunlight_choices', [])
        soil_choices = kwargs.pop('soil_choices', [])
        super().__init__(*args, **kwargs)
        self.fields['sunlight'].choices = sunlight_choices
        self.fields['soil'].choices = soil_choices
