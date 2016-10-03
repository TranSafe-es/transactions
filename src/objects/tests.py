from django.test import TestCase
from rest_framework.test import APIClient
import uuid


class ObjectsTestCase(TestCase):
    def setUp(self):
        pass

    def test_objects(self):
        client = APIClient()

        to_uuid = str(uuid.uuid4())

        url = "/api/v1/object/new/"
        data = {'name': 'Lote Terreno Hotel ou similar Alto Alentejo Marvao - Proje. Aprovado',
                'url': 'https://www.olx.pt/anuncio/lote-terreno-hotel-ou-similar-alto-alentejo-marvo-proje-aprovado-IDzGYf3.html#d62794f553;promoted',
                'identifier': to_uuid}
        response = client.post(path=url, data=data)
        self.assertEqual(response.status_code, 201)

        url = "/api/v1/object/list/"+to_uuid+"/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        object_id = response.data[0]["id"]
        url = "/api/v1/object/details/"+object_id+"/"
        response = client.get(path=url)
        self.assertEqual(response.status_code, 200)
