
from .models import Notification

def notification(request):
  if request.user.is_authenticated:
    return {'notifications': request.user.notifications.filter(is_read=False)}

  else: 
    return {'notifications': []}




    