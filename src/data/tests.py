from django.test import TestCase
from rest_framework.test import APIClient
import uuid


class ObjectsTestCase(TestCase):
    def setUp(self):
        pass

    def test_objects(self):
        client = APIClient()

        # create object

        buyer_uuid = str(uuid.uuid4())

        url = "/api/v1/object/new/"
        data = {'name': 'Lote Terreno Hotel ou similar Alto Alentejo Marvao - Proje. Aprovado',
                'url': 'https://www.olx.pt/anuncio/lote-terreno-hotel-ou-similar-alto-alentejo-marvo-proje-aprovado-IDzGYf3.html#d62794f553;promoted',
                'user_uuid': buyer_uuid}
        response = client.post(path=url, data=data)
        self.assertEqual(response.status_code, 201)

        seller_uuid = str(uuid.uuid4())
        object_uuid = response.data["id"]

        # create transaction

        url = "/api/v1/transaction/new/"
        data = {'buyer_uuid': buyer_uuid,
                'seller_uuid': seller_uuid,
                'object_uuid': object_uuid,
                'price': 21.2,
                'state': "AWAITING_SELLER_CONFIRMATION"}
        response = client.post(path=url, data=data)
        self.assertEqual(response.status_code, 201)

        transaction_uuid = response.data["id"]

        # transaction details

        url = "/api/v1/transaction/details/" + transaction_uuid + "/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)

        # transaction history as seller

        url = "/api/v1/transaction/history/"+seller_uuid+"/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["as_seller"]), 1)

        # transaction history as buyer

        url = "/api/v1/transaction/history/"+buyer_uuid+"/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["as_buyer"]), 1)

        # update transaction state

        url = "/api/v1/transaction/state/"
        data = {'transaction_id': transaction_uuid,
                'state': "REFUND"}
        response = client.post(path=url, data=data)
        self.assertEqual(response.status_code, 200)
