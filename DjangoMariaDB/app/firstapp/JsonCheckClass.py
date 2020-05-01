#from django.http import HttpResponse
#from django.http import JsonResponse
import json

class CheckJson():

    def isJsonCheck(self,myjson):
        try:
            json_object = json.loads(myjson)
        except ValueError as e:
            return False
            #response_data = {}
            #response_data['result'] = 'error'
            #response_data['message'] = 'invalid Json'
            #return JsonResponse(response_data, status=400)
        return True
