import io
import requests
import zipfile
from django.http import HttpResponse

# TODO: add error catching

GpsServiceUrl = "http://156.56.174.162:8000/gpsservice/kml?"
KmlPrefix = "http://156.56.174.162:8000/static"
WoForecastUrl = 'http://www.openhazards.com/Tools/kml/wo-forecast.kmz'
CaForecastUrl = 'http://www.openhazards.com/Tools/kml/ca-forecast.kmz'


def gps_service(request):
    if request.method == 'GET':
        print(request.GET.get("data"))
        # more efficient way of getting request params?
        # getting request params from GET in GNSS.vue
        payload = {
            "function": request.GET.get("function"),  # .GET.get("function"),
            "lat": request.GET.get("lat"),
            "lon": request.GET.get("lon"),
            "width": request.GET.get("width"),
            "height": request.GET.get("height"),
            "epoch": request.GET.get("epoch"),
            "epoch1": request.GET.get("epoch1"),
            "epoch2": request.GET.get("epoch2"),
            "scale": request.GET.get("scale"),
            "ref": request.GET.get("ref"),
            "ct": request.GET.get("ct"),
            "pt": request.GET.get("pt"),
            "dwin1": request.GET.get("dwin1"),
            "dwin2": request.GET.get("dwin2"),
            "prefix": request.GET.get("prefix"),
            "mon": request.GET.get("mon"),
            "eon": request.GET.get("eon"),
            "vabs": request.GET.get("vabs")}
        print(payload)
        data = requests.get(GpsServiceUrl, params=payload)
        responseData = HttpResponse(data)
        return responseData


def get_gnss_kml(request):
    if request.method == 'GET':
        folder = request.GET.get("folder")
        file = request.GET.get("file")
        url = KmlPrefix + '/' + folder + '/' + file
        print('url:' + url)
        data = requests.get(url)
        responseData = HttpResponse(data)
        return responseData


# TODO combine below methods

def wo_forecast(request):
    if request.method == 'GET':
        data = requests.get(WoForecastUrl, stream=True)
        z = zipfile.ZipFile(io.BytesIO(data.content))
        responseData = HttpResponse(z.open('doc.kml'))
        return responseData


def ca_forecast(request):
    if request.method == 'GET':
        data = requests.get(CaForecastUrl, stream=True)
        z = zipfile.ZipFile(io.BytesIO(data.content))
        responseData = HttpResponse(z.open('doc.kml'))
        return responseData


