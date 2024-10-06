#---------------------------------------------------------------------
# TRT Watersystem website Views definitions
#
# A2 Hosting installation
# see settings.py
#---------------------------------------------------------------------

from datetime import datetime
from django.utils import timezone
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
import logging

from TRT_watersystem.models import Watersystem

tz = timezone.get_current_timezone()
dateTimeStr = '%Y-%m-%d %H:%M:%S'
adminEmail = "volker.petersen01@gmail.com"

# Get an instance of a logger
logger = logging.getLogger('myLogger')

def get_DateTime():
    """---------------------------------------------------------------------
        function to current date and time with Timezone information
        The time is rounded down to full seconds

        Args:
            None

        Return:
            datetime object
    """
    now = datetime.now()
    now = now.replace(microsecond=0)
    now = now.replace(tzinfo=tz)
    return now

def initialize_settings(request):
    """---------------------------------------------------------------------
        function to create a settings dictionary with data to be passed 
        into all html files

        Args:
            None

        Return:
            content (dictionary): dictonary holding the settings data
    """

    site = "TRT Watersystem"
    siteLong = "Territory HOA Watersystem"
    css = "css/trt_main.css?v"+datetime.now().strftime(dateTimeStr)
    js = "js/trt_main.js?v="+datetime.now().strftime(dateTimeStr)

    today = get_DateTime()
    year = today.year

    content = {
        "site": site,
        "siteLong": siteLong,
        "css": css,
        "js": js,
        "adminEmail": adminEmail,
    }

    currentSite = get_current_site(request)
    protocol = request.scheme
    content['domain'] = f"{protocol}://{currentSite.domain}"

    return content


def index(request):
    """---------------------------------------------------------------------
        view function for the TRT Watersystem home page
    """
    content = initialize_settings(request)
    
    today = get_DateTime().date()

    allRecords = Watersystem.objects.all().order_by('-date')

    content['allRecords'] = allRecords

    return render(
        request,
        "TRT_watersystem/index.html",
        context=content)


# add custom error pages
def error_404(request, exception=None):
    return render(request, 'errors/404.html', context={})


def error_500(request):
    content = {'webmasterEmail': adminEmail}
    return render(request, 'errors/500.html', context=content)

