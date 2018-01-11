from django.http import HttpResponse, Http404
import datetime

from django.shortcuts import render_to_response
from django.template import Template, Context
from django.template.loader import get_template


def hello(request):
    return HttpResponse('hello word')

def current_time(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.</body></html>' % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In %s hours, it will be %s.</body></html>' % (offset, dt)
    return HttpResponse(html)

def current_datetime(request):
    # now =  datetime.datetime.now()
    # # t = Template('<html><body>It is now {{ current_date }}</body></html>')
    # # t = get_template('current_datetime.html')
    # # html = t.render({'current_data': now})
    # # return HttpResponse(html)
    # return render_to_response('current_datetime.html', {'current_date': now})
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())

