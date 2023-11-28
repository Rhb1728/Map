import json
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
# from .models import Information, LoginInfo
from django.contrib.auth.models import User, auth
from InteractiveMap.models import AddInfo
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.
flag = 0
# @login_required
def home(request):
    print(request.user.is_authenticated)
    if flag == 1:
        return render(request, 'home.html')
    else:
        return HttpResponse("Please log in first")

    
def create(request):
    user = request.user
    if request.method == 'POST':
        setColor = request.POST.get('setColor')
        setLocation = request.POST.get('setLocation')
        setProfile = request.POST.get('setProfile')
        setRegistered = request.POST.get('setRegistered')
        setCare = request.POST.get('setCare')
        setICB = request.POST.get('setICB')
        setAgreements = request.POST.get('setAgreements')
        setNotes = request.POST.get('setNotes')
        setMapID = request.POST.get('setMapID')

        new_info = AddInfo(mapID = setMapID,location = setLocation,profile_of_needs = setProfile,registered_providers = setRegistered,care_providers = setCare,icb_contacts = setICB,void_agreement = setAgreements,additional_notes = setNotes,color =setColor,user=user)
        new_info.save()
        # check if info is adding or not
        # all_objects = AddInfo.objects.all()
        # for obj in all_objects:
        #     print(f"Map ID: {obj.mapID}")
        #     print(f"Location: {obj.location}")
        #     print(f"Profile of Needs: {obj.profile_of_needs}")
        #     print(f"Registered Providers: {obj.registered_providers}")
        #     print(f"Care Providers: {obj.care_providers}")
        #     print(f"ICB Contacts: {obj.icb_contacts}")
        #     print(f"Void Agreement: {obj.void_agreement}")
        #     print(f"Additional Notes: {obj.additional_notes}")
        #     print(f"Color: {obj.color}")
        #     print("-----------------------------")
        objects_with_same_mapID = AddInfo.objects.filter(mapID=setMapID,user=user)

        # Update the color of all retrieved objects
        for obj in objects_with_same_mapID:
            obj.color = setColor
            obj.save()

    return render(request, 'home.html')

def get_info_data(request):
    user = request.user
    if request.method == 'GET':
        map_id = request.GET.get('mapID')
        if map_id:
            filtered_data = AddInfo.objects.filter(mapID=map_id, user=user)
            data = list(filtered_data.values())  # Convert QuerySet to a list of dictionaries
            return JsonResponse(data, safe=False)
    
    return JsonResponse([], safe=False)

def loginn(request):
    global flag
    flag = 0
    message = 'Welcome to Interactive Map'
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        
        user = authenticate(username=username, password=password)
        
        if user is not None: 
            login(request, user)
            flag = 1
            return redirect('home')  
        
   
    return render(request, 'login.html')

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        obj_to_delete = AddInfo.objects.get(id=id)
        obj_to_delete.delete()  

    return render(request, 'home.html')


def update_data(request):
   
    if request.method == 'POST':
        id = request.POST.get('id')
        location = request.POST.get('location')
        profile_of_needs = request.POST.get('profile_of_needs')
        registered_providers = request.POST.get('registered_providers')
        care_providers = request.POST.get('care_providers')
        icb_contacts = request.POST.get('icb_contacts')
        void_agreement = request.POST.get('void_agreement')
        additional_notes = request.POST.get('additional_notes')
        
        obj_to_edit = AddInfo.objects.get(id=id)
        obj_to_edit.location = location
        obj_to_edit.profile_of_needs = profile_of_needs
        obj_to_edit.registered_providers = registered_providers
        obj_to_edit.care_providers = care_providers
        obj_to_edit.icb_contacts = icb_contacts
        obj_to_edit.void_agreement = void_agreement
        obj_to_edit.additional_notes = additional_notes
        obj_to_edit.save()
        


    return render(request, 'home.html')
    