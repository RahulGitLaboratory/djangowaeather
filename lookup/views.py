# This is my views.py file 

from django.shortcuts import render
from dotenv import load_dotenv
import os

load_dotenv()

# Create your views here.

def home(request):
    import json
    import requests
    API_KEY = os.getenv("API_KEY")

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        # return render(request, 'home.html', {'zipcode' : zipcode})

        api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY={API_KEY}")
        
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error...."

        if  api[0]["Category"]["Name"] == "Good":
            catagory_description = 'Air quality is satisfactory, and air pollution poses little or no risk. Enjoy your activity outside.'
            catagory_color = 'good'
            
        elif  api[0]["Category"]["Name"] == "Moderate":
            catagory_description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
            catagory_color = 'moderate'
            
        elif  api[0]["Category"]["Name"] == "Unhealthy for Sensitive Groups":
            catagory_description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
            catagory_color = 'usg'
            
        elif  api[0]["Category"]["Name"] == "Unhealthy":
            catagory_description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
            catagory_color = 'unhealthy'
            
        elif  api[0]["Category"]["Name"] == "Very Unhealthy":
            catagory_description = 'Health alert: The risk of health effects is increased for everyone.'
            catagory_color = 'veryunhealthy'
            
        elif  api[0]["Category"]["Name"] == "Hazardous":
            catagory_description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
            catagory_color = 'hazardous'
            
        return render(request, 'home.html', {'api' : api, 'catagory_description' : catagory_description, 'catagory_color' : catagory_color})


    else:
        api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY={API_KEY}")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error...."

        if  api[0]["Category"]["Name"] == "Good":
            catagory_description = 'Air quality is satisfactory, and air pollution poses little or no risk. Enjoy your activity outside.'
            catagory_color = 'good'
            
        elif  api[0]["Category"]["Name"] == "Moderate":
            catagory_description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
            catagory_color = 'moderate'
            
        elif  api[0]["Category"]["Name"] == "Unhealthy for Sensitive Groups":
            catagory_description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
            catagory_color = 'usg'
            
        elif  api[0]["Category"]["Name"] == "Unhealthy":
            catagory_description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
            catagory_color = 'unhealthy'
            
        elif  api[0]["Category"]["Name"] == "Very Unhealthy":
            catagory_description = 'Health alert: The risk of health effects is increased for everyone.'
            catagory_color = 'veryunhealthy'
            
        elif  api[0]["Category"]["Name"] == "Hazardous":
            catagory_description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
            catagory_color = 'hazardous'
            
        return render(request, 'home.html', {'api' : api, 'catagory_description' : catagory_description, 'catagory_color' : catagory_color})
def about(request):
    return render(request, 'about.html', {})