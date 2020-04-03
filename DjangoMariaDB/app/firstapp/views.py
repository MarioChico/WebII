# Create your views here.
#IMPORT models
from .models import Movie,ApiUsers

#IMPORT LIBRARIRES/FUNCTIONS
#from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
from firstapp.JsonCheck import *
from firstapp.customClasses import *
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password

def makepassword(request,password):
    hashPassword = make_password(password)
    response_data = {}
    response_data['password'] = hashPassword
    return JsonResponse(response_data, status=200)

def login(request):

    #VALIDATE METHOD
    if request.method == 'POST':
        #DECLARE RESPONSE
        responseData = {}
        #CHECK JSON STRUCTURE
        isJson = isJson(request.body)
        if isJson == True:
            json_data = json.loads(request.body)
            response_data['result'] = 'success'
            response_data['message'] = 'valid Json'
            return JsonResponse(response_data, status=400)
            #CHECK JSON CONTENT
            attr_error = False
            if 'user' not in json_data:
                attr_error = True
            elif 'password' not in json_data:
               attr_error = True


            if attr_error == True:
                  response_data = {}
                  response_data['result'] = 'Error'
                  response_data['message'] = 'User or password is required'
                  return JsonResponse(response_data, status=200)
            else:
                response_data = {}
                response_data['result'] = 'success'
                response_data['message'] = 'valid Json'
                return JsonResponse(response_data, status=400)
            #CHECK IF USER EXITST
            try:
                usuario = json_data['user']
                obj = ApiUsers.objects.get(usuario)
                response_data['result'] = 'success'
                return JsonResponse(response_data, status=200)
            except ApiUsers.DoesNotExist:
                response_data['result'] = 'error'
                response_data['message'] = 'USER NOT FOUND'
                return JsonResponse(response_data, status=400)
            #TAKE PASSWORD OF THE USER
            password = json_data['password']
            hashPwd = obj.password
            #CHECK IF PASSWORD IS CORRECT
            if password == True and hashPwd == True:
                response_data['result'] = 'success'
                response_data['message'] = 'VALID KEYS'
                return JsonResponse(response_data, status=200)
            else:
                response_data['result'] = 'success'
                response_data['message'] = 'VALID KEYS'
                return JsonResponse(response_data, status=401)
            #CHECK IF USER HAS API-KEY
            if obj.api_key==True:
                newApiKey = ApiKey().generate_key_complex()
                obj.api_key = newApiKey
                obj.save()
            #RETURN RESPONSE
            responseData['result'] = 'success'
            responseData['message'] = 'VALID USER'
            response_data['userApikey'] = obj.api_key
            return JsonResponse(responseData, status=200)

        else:
            response_data['result'] = 'error'
            response_data['message'] = 'invalid Json'
            return JsonResponse(response_data, status=200)
    else:
        responseData = {}
        responseData['result'] = 'error'
        responseData['message'] = 'Invalid Request'
        return JsonResponse(responseData, status=400)


def showMovies(request):

    #VALIDATE METHOD
    if request.method == 'POST':
        #DECLARE RESPONSE
        response_data = {}
        validateKey = ApiKey().check(request)
        if validateKey == True:
            return JsonResponse(validateKey, status =200)
        #CHECK JSON STRUCTURE
        checking_json = checkJson().isJson(request.body)
        #isJson = is_Json(request.body)
        if checking_json == False:
            response_data['result'] = 'error'
            response_data['message'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
        json_data = json.loads(request.body)
            #CHECK JSON CONTENT
        attr_error = False
        attrErrorMssg = ""
        if 'user' not in json_data:
            attr_error = True
            attrErrorMssg = "The user is required"
        elif 'password' not in json_data:
            attr_error = True
            attrErrorMssg = "The password is required"

        if attr_error == True:
            response_data = {}
            response_data['result'] = 'Error'
            response_data['message'] = attrErrorMssg
            return JsonResponse(response_data, status=401)
        else:
            response_data = {}
            response_data['result'] = 'success'
            response_data['message'] = 'Valid Json'
            return JsonResponse(response_data, status=200)
            #CHECK IF USER EXITST
        validUser = ClientExists().ValidateUser(json_data)
        if validUser[0] != True:
            return validUser[1]
        obj = validUser[1]

            #TAKE PASSWORD OF THE USER
        password = json_data['password']
        hashPwd = obj.password
            #CHECK IF PASSWORD IS CORRECT
        if password == True and hashPwd == True:
            response_data['result'] = 'success'
            response_data['message'] = 'VALID KEYS'
            return JsonResponse(response_data, status=200)
        else:
            response_data['result'] = 'error'
            response_data['message'] = 'INVALID KEYS'
            return JsonResponse(response_data, status=401)
            #CHECK IF USER HAS API-KEY
        if obj.api_key==request.headers["user-api-key"]:
            response_data['result'] = 'success'
            response_data['message'] = 'VALID KEYS'
            return JsonResponse(response_data, status=200)

        responseData['result'] = 'success'
        movies = Movie.objects.all()
        movieResult = []
        for i in movies:
            movie = {}
            movie['id'] = i.movieid
            movie['title'] = i.movietitle
            movie['description'] = i.description
            movie['releaseDate'] = i.releasedate
            movie['imageUrl'] = i.imageurl
            movieResult.append(movie)
        response_data['movies'] = movieResult
        return JsonResponse(response_data,status=200)
    else:
        responseData = {}
        responseData['result'] = 'error'
        responseData['message'] = 'Invalid Request'
        return JsonResponse(responseData, status=400)
