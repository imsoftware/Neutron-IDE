from django.conf import settings

import ide.settings

import time

class Track (object):
  def process_request (self, request):
    request.track = True
    request.track_code = ide.settings.IDE_TRACK_CODE
    
    if settings.DEBUG:
      request.track = False
      
    elif not ide.settings.IDE_TRACK:
      request.track = False
      
    return None
    
class Logging (object):
  def process_response (self, request, response):
    if request.META.has_key('SERVER_SOFTWARE'):
      if 'CherryPy' in request.META['SERVER_SOFTWARE']:
        if request.is_secure():
          secure = 'SSL'
          
        else:
          secure = 'UNSECURE'
          
        print "[%s] \"%s %s\" %d %d %s" % (time.strftime("%d/%b/%Y %H:%M:%S", time.localtime()), request.method, request.get_full_path(), response.status_code, len(response.content), secure)
        
    return response
    
