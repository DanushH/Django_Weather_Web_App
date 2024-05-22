import urllib.request
import json
from django.shortcuts import render
from django.conf import settings
from django.views import View
from django.http import HttpRequest, HttpResponse


class IndexView(View):
    template_name = "main/index.html"
    api_key = settings.API_KEY

    def get(self, request: HttpRequest) -> HttpResponse:
        return self.render_response(request)

    def post(self, request: HttpRequest) -> HttpResponse:
        city = request.POST.get("city")

        data = self.fetch_weather_data(city)
        return self.render_response(request, data)

    def fetch_weather_data(self, city: str) -> dict:
        source = urllib.request.urlopen(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={self.api_key}"
        ).read()
        data_list = json.loads(source)

        data = {
            "city": city,
            "temp": f"{round(data_list['main']['temp'])}°C",
            "pressure": f"{data_list['main']['pressure']}Pa",
            "humidity": f"{data_list['main']['humidity']}%",
            "main": data_list["main"],
            "icon": data_list["weather"][0]["icon"],
            "description": data_list["weather"][0]["description"],
        }

        return data

    def render_response(self, request: HttpRequest, data: dict = None) -> HttpResponse:
        if data is None:
            data = {}
        print(data)
        return render(request, self.template_name, data)
