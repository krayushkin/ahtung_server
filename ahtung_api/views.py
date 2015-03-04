from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View
from django.http import HttpResponse
from django.core import serializers
from ahtung_api.models import Person, Group, Signal, EnabledSignal
from ahtung_api.populate_db import populate
from json import dumps, loads
from uuid import uuid4
from ahtung_api.gcm import send_signal

class AhtungApi:
    COMMAND_GET_USERS = "get_users"
    COMMAND_JOIN_GROUP = "join_group"
    COMMAND_LEAVE_GROUP = "leave_group"
    COMMAND_CREATE_GROUP = "create_group" # registration_id, name, enabled_signals
    COMMAND_SEND_SIGNAL = "send_signal"
    
    RESPONSE_STATUS_OK = 0
    RESPONSE_STATUS_ERROR = 1


class PopulateView(View):
    def get(self, request, *args, **kwargs):
        populate()
        return HttpResponse("populated")


class ApiView(View):
    template_name = "test.js"

    func_name = "UNSUPPORTED"
    func_args = {}
    r = None

    def post(self, request, *args, **kwargs):

        params = request.GET
        action = kwargs["action"]
        r = {"status": 1, "data": {}}

        if action == AhtungApi.COMMAND_JOIN_GROUP:
            group_id = params['group_id']
            registration_id = params['registration_id']
            name = params['name']
            group = Group.objects.get(group_id__exact=group_id)
            person = Person(group=group, name=name, registration_id=registration_id)
            person.save()
            r["status"] = 0

        elif action == AhtungApi.COMMAND_LEAVE_GROUP:
            registration_id = params['registration_id']
            person = Person.objects.get(registration_id__exact=registration_id)
            person.delete()
            r["status"] = 0

        elif action == AhtungApi.COMMAND_CREATE_GROUP:
            group_repr = loads(request.body.decode("utf-8"))
            group = Group(group_id="{0:x}".format(uuid4().time_low))
            group.save()
            signals = [Signal.objects.get(name__exact=signal) for signal in group_repr["signals"]]
            for signal in signals:
                en_sig = EnabledSignal(group=group, signal=signal)
                en_sig.save()
            r["status"] = 0
            r["data"]["group_id"] = group.group_id

        elif action == AhtungApi.COMMAND_SEND_SIGNAL:
            registration_id = params['registration_id']
            signal = params["signal"]
            person = Person.objects.get(registration_id__exact=registration_id)
            persons = Person.objects.filter(group=person.group)
            r["status"] = 0
            r["data"]["persons"] = [p.name for p in persons]
            send_signal([p.registration_id for p in persons], signal)

        data = dumps(r)
        return HttpResponse(data, content_type="text/json")

    def get(self, request, *args, **kwargs):
        params = request.GET
        action = kwargs['action']

        r = {"status": 1, "data": {}}
    
        if action == AhtungApi.COMMAND_GET_USERS:
            group_id = params['group_id']
            users = Person.objects.filter(group__group_id__exact=group_id)
            r["data"]["persons"] = [p.name for p in users]
            r["status"] = 0

        data = dumps(r)
        return HttpResponse(data, content_type="text/json")
