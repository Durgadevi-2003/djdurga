import pickle
import numpy as np
from django.shortcuts import render
from .forms import PlantInputForm

# Load model and encoders once
with open("model/model.pkl", "rb") as f:
    model, label_encoders, feature_columns = pickle.load(f)

def predict_growth(request):
    sunlight_options = [(i, val) for i, val in enumerate(label_encoders['Sunlight'].classes_)]
    soil_options = [(i, val) for i, val in enumerate(label_encoders['Soil'].classes_)]
    
    if request.method == "POST":
        form = PlantInputForm(request.POST, sunlight_choices=sunlight_options, soil_choices=soil_options)
        if form.is_valid():
            # Collect form data
            plant_name = form.cleaned_data['plant_name']  # Adding plant name
            temperature = form.cleaned_data['temperature']
            sunlight = int(form.cleaned_data['sunlight'])
            soil = int(form.cleaned_data['soil'])
            humidity = form.cleaned_data['humidity']
            
            # Prepare features for prediction
            features = np.array([[temperature, sunlight, soil, humidity]])  # 4 features
            
            # Make prediction
            prediction = model.predict(features)[0]
            
            # Decode the growth label
            growth = label_encoders["Growth"].inverse_transform([prediction])[0]
            
            # Get prediction probabilities
            probs = model.predict_proba(features)[0]
            prob_dict = {
                label: prob for label, prob in zip(label_encoders["Growth"].classes_, probs)
            }
            
            # Create a descriptive result
            growth_description = {
                "slow": "The plant is growing slowly. Ensure it's getting enough water and nutrients.",
                "moderate": "The plant is growing at a moderate pace. It's doing well.",
                "fast": "The plant is growing quickly! Keep an eye on its water and light needs."
            }
            
            result_description = growth_description.get(growth, "Growth rate is unknown.")
            
            # Return the result with prediction and probabilities
            return render(request, "predictor/form.html", {
                "form": form,
                "result": growth,
                "result_description": result_description,
                "probabilities": prob_dict,
                "plant_name": plant_name
            })

    else:
        form = PlantInputForm(sunlight_choices=sunlight_options, soil_choices=soil_options)

    return render(request, "predictor/form.html", {"form": form})
