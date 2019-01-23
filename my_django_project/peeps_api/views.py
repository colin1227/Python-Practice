from django.http import JsonResponse

from django.views.generic import View
from .models import People

from django.views.decorators.csrf import ensure_csrf_cookie , csrf_exempt
from django.utils.decorators import method_decorator

import json
import datetime

# Create your views here.

class Login(View):
    @csrf_exempt
    def dispatch(self, req, *args, **kwargs):
        return super(Login, self).dispatch(req, *args, **kwargs)
    
    def post(self, req):
        if req.method == "POST":
            data = req.body.decode('utf-8')
            data = json.loads(data)
        
            user = People.objects.get(first_name = data.get('first_name'))
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

class Register(View):
    @csrf_exempt
    def dispatch(self, req, *args, **kwargs):
        return super(Register, self).dispatch(req, *args, **kwargs)
    
    def post(self, req):
        if req.method == "POST":
            data = req.body.decode('utf-8')
            data = json.loads(data)
            try:
                new_user = People(first_name = data.get('first_name'),
                 last_name = data.get('last_name'),
                 age = data.get('age'),
                 birth_year = data.get('birth_year'),
                 birth_month = data.get('birth_month'),
                 birth_day = data.get('birth_day'))
                new_user.save()
                return JsonResponse(
                    {'Content-Type':'application/json',
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'loggedIn': True,
                    'status': 200
                    }, safe=False)
            except:
                return JsonResponse({
                    'loggedIn': False
                    }, safe=False)
        
class User_detail(View):
    @csrf_exempt
    def dispatch(self, req, *args, **kwargs):
        return super(Birthdays, self).dispatch(req, *args, **kwargs)
    
    def get(self, req, pk):
        user = People.objects.get(pk=pk)
        return JsonResponse({'data': user}, safe=False)

    def delete(self, req, pk):
        try:
            user = People.objects.get(pk=pk)
            user.delete()
            return JsonResponse({'status': 200}, safe=False)
        except People.DoesNotExist:
            return JsonResponse({'status':500}, safe=False)
        except:
            return JsonResponse({'status':500}, safe=False)

class Birthdays(View):
    @ensure_csrf_cookie
    
    def dispatch(self, req, *args, **kwargs):
        return super(Birthdays, self).dispatch(req, *args, **kwargs)
    
    def get(self, req):
        try:
            now = datetime.datetime.now()
            everyone = list(People.objects)
            for person in everyone:
                if(now.strftime("%m") == person.birth_month):
                    if(now.strftime("%d") == person.birth_day):
                        person.age += 1
                        person.save()
            everyone.save()
            return JsonResponse({'status': 200, 'data': everyone}, safe=False)

        except People.DoesNotExist:
            return JsonResponse({"status": 500}, safe=False)
        except:
            return JsonResponse({"status": 500}, safe=False)
   
