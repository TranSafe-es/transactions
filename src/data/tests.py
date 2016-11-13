from django.test import TestCase
from rest_framework.test import APIClient
import uuid


class ObjectsTestCase(TestCase):
    def setUp(self):
        pass

    def test_objects(self):
        client = APIClient()

        app_name = "teste"
        url = "/api/v1/register/app/"
        data = {"name": app_name}
        response = client.post(path=url, data=data)
        token = response.data["token"]

        to_uuid = str(uuid.uuid4())

        # create object
        url = "/api/v1/object/new/?token="+token
        data = {'name': 'Lote Terreno Hotel ou similar Alto Alentejo Marvao - Proje. Aprovado',
                'url': 'https://www.olx.pt/anuncio/lote-terreno-hotel-ou-similar-alto-alentejo-marvo-proje-aprovado-IDzGYf3.html#d62794f553;promoted',
                'identifier': to_uuid}
        response = client.post(path=url, data=data)
        self.assertEqual(response.status_code, 201)

        url = "/api/v1/object/new/?token="+token
        data = {'name': 'Lote Terreno Hotel ou similar Alto Alentejo Marvao - Proje. Aprovado',
                'url': 'https://www.olx.pt/anuncio/lote-terreno-hotel-ou-similar-alto-alentejo-marvo-proje-aprovado-IDzGYf3.html#d62794f553;promoted',
                'identifier': to_uuid}
        response = client.post(path=url, data=data)
        self.assertEqual(response.status_code, 302)

        from_uuid = str(uuid.uuid4())
        object_uuid = response.data["id"]

        # create transaction

        url = "/api/v1/transaction/new/?token="+token
        data = {'to_uuid': to_uuid,
                'from_uuid': from_uuid,
                'object_uuid': object_uuid,
                'price': 21.2,
                'state': "AWAITING_CONFIRMATION"}
        response = client.post(path=url, data=data)
        self.assertEqual(response.status_code, 201)

        url = "/api/v1/transaction/new/?token="+token
        data = {'to_uuid': to_uuid,
                'from_uuid': from_uuid,
                'object_uuid': object_uuid,
                'price': 21.2,
                'state': "AWAITING_CONFIRMATION"}
        response = client.post(path=url, data=data)
        self.assertEqual(response.status_code, 201)

        transaction_uuid = response.data["id"]

        # transaction details

        url = "/api/v1/transaction/details/" + transaction_uuid + "/?token="+token
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)

        # transaction history as from

        url = "/api/v1/transaction/history/"+from_uuid+"/?token="+token
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["from_uuid"]), 2)

        # transaction history as to

        url = "/api/v1/transaction/history/"+to_uuid+"/?token="+token
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["to_uuid"]), 2)

        # update transaction state

        url = "/api/v1/transaction/state/?token="+token
        data = {'transaction_id': transaction_uuid,
                'state': "REFUND"}
        response = client.post(path=url, data=data)
        self.assertEqual(response.status_code, 200)

        # add tracking code
        url = "/api/v1/transaction/tracking_code/?token="+token
        data = {'transaction_id': transaction_uuid,
                'tracking_code': "OC144693436PT"}
        response = client.post(path=url, data=data)
        self.assertEqual(response.status_code, 200)

        # get stats about the transactions
        url = "/api/v1/transaction/stats/?token="+token
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
