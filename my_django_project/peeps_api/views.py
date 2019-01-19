from django.http import JsonResponse

from django.views.generic import View
from .models import People

from django.views.decorators.csrf import ensure_csrf_cookie , csrf_exempt
from django.utils.decorators import method_decorator

import json
import datetime

# Create your views here.

class Accounts(View):
    print("happens")
    @csrf_exempt
    def dispatch(self, req, *args, **kwargs):
        return super(Accounts, self).dispatch(req, *args, **kwargs)
    
    def post(self, req):
        data = req.body.decode('utf-8')
        data = json.loads(data)
        
        user = People.objects.get(first_name = data.get('first_name'))
        print(user.first_name, user.last_name)
        if(user.last_name == data.get('last_name')):
            return JsonResponse(
                {'Content-Type':'application/json',
                'first_name': user.first_name,
                'last_name': user.last_name,
                'loggedIn': True,
                'status': 200
                }, safe=False)
        else:
            return JsonResponse({'loggedIn': False}, safe=False)

now = datetime.datetime.now()

class Birthdays(View):
    @ensure_csrf_cookie
    
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
   
