# -*- encoding: utf-8 -*-

from django.test import TestCase, Client

# Create your tests here.
from ahtung_api.models import Person, Group, Signal, EnabledSignal
from json import loads, dumps
from urllib.parse import urlencode


class AnimalTestCase(TestCase):
    def setUp(self):
        s1 = Signal(name="Alarm", signal_id="1")
        s2 = Signal(name="Warning", signal_id="2")
        s3 = Signal(name="Cancel", signal_id="3")
        
        s1.save()
        s2.save()
        s3.save()

        g1 = Group(group_id='123123')
        g2 = Group(group_id='123124')

        g1.save()
        g2.save()

        en1 = EnabledSignal(group=g1, signal=s1)
        en2 = EnabledSignal(group=g1, signal=s2)
        en3 = EnabledSignal(group=g1, signal=s3)

        en4 = EnabledSignal(group=g2, signal=s1)
        en5 = EnabledSignal(group=g2, signal=s3)

        en1.save()
        en2.save()
        en3.save()
        en4.save()
        en5.save()

        u1 = Person(name=u"Вася Пупкин", group=g1, registration_id='12353')
        u2 = Person(name=u"Иван Помидоров", group=g1, registration_id='45678')
        u3 = Person(name=u"Коля Иванов", group=g1, registration_id='457932')
        u4 = Person(name=u"Женя Некрасов", group=g2, registration_id='122345')
        u5 = Person(name=u"Галя Петрова", group=g2, registration_id='578632')

        u1.save()
        u2.save()
        u3.save()
        u4.save()
        u5.save()

    def test_action_get_users(self):
        c = Client()
        r = c.get("/api/get_users", {'action': 'get_users', 'group_id': '123123'})
        o = loads(r.content.decode("utf-8"))
        self.assertDictEqual(o, {"status": 0, "data": {"persons": ["Вася Пупкин", "Иван Помидоров", "Коля Иванов"]}})

        r = c.get("/api/get_users", {'action': 'get_users', 'group_id': '123124'})
        o = loads(r.content.decode("utf-8"))
        self.assertDictEqual(o, {"status": 0, "data": {"persons": ["Женя Некрасов", "Галя Петрова"]}})

    def test_join_group(self):
        c = Client()
        params = urlencode({"group_id": "123124", "registration_id": "21234678", "name": "Дима Краюшкин"})
        r = c.post("/api/join_group?%s" % params)
        o = loads(r.content.decode("utf-8"))
        self.assertEqual(o["status"], 0)

        r = c.get("/api/get_users", {'action': 'get_users', 'group_id': '123124'})
        o = loads(r.content.decode("utf-8"))
        self.assertDictEqual(o, {"status": 0, "data": {"persons": ["Женя Некрасов", "Галя Петрова", "Дима Краюшкин"]}})

    def test_leave_group(self):
        c = Client()
        # delete Galya
        params = urlencode({"registration_id": "578632"})
        r = c.post("/api/leave_group?%s" % params)
        o = loads(r.content.decode("utf-8"))
        self.assertEqual(o["status"], 0)

        r = c.get("/api/get_users", {'action': 'get_users', 'group_id': '123124'})
        o = loads(r.content.decode("utf-8"))
        self.assertDictEqual(o, {"status": 0, "data": {"persons": ["Женя Некрасов"]}})

    def test_create_group(self):
        c = Client()
        # delete Galya
        params = urlencode({"registration_id": "578632"})
        en_signals = ["Warning", "Cancel"]
        request_body = dumps({"signals": en_signals})
        r = c.post("/api/create_group?%s" % params, request_body, content_type="application/json")
        o = loads(r.content.decode("utf-8"))
        self.assertEqual(o["status"], 0)
        new_group_id = o["data"]["group_id"]

        params = urlencode({"group_id": new_group_id, "registration_id": "21234678", "name": "Дима Краюшкин"})
        r = c.post("/api/join_group?%s" % params)
        o = loads(r.content.decode("utf-8"))
        self.assertEqual(o["status"], 0)
        g = Group.objects.get(group_id__exact=new_group_id)
        self.assertListEqual([en_sig.signal.name for en_sig in EnabledSignal.objects.filter(group=g)], en_signals)

    def test_send_signal(self):
        c = Client()

        params = urlencode({"registration_id": "45678", "signal": "Warning"})
        r = c.post("/api/send_signal?%s" % params)
        o = loads(r.content.decode("utf-8"))
        self.assertEqual(o["status"], 0)
        self.assertListEqual(o["data"]["persons"], ["Вася Пупкин", "Иван Помидоров", "Коля Иванов"])







        

        

