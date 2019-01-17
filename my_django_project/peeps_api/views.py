from django.http import JsonResponse

from django.views import View
from .models import People

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json
import datetime

# Create your views here.

now = datetime.datetime.now()

class Birthdays(View):
    @method_decorator(csrf_exempt)
    
    def dispatch(self, req, *args, **kwargs):
        return super(Birthdays, self).dispatch(req, *args, **kwargs)
    
    def new_day(self, req):
        try:
            everyone = list(People.objects)
            for person in everyone:
                if(now.strftime("%m") == person.birth_month):
                    if(now.strftime("%d") == person.birth_day):
                        person.age += 1
                        person.save()
            everyone.save()
            return JsonResponse({'status': 200}, safe=False)

        except People.DoesNotExist:
            return JsonResponse({"error":"doesnt exist pal"}, safe=False)
        except:
            return JsonResponse({"error": "not valid data"}, safe=False)
   
