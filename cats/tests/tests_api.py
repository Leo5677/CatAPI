import requests


class TestCatsAPI:
    headers = {'Authorization': 'Token c644ba60874114c8f8f53e9aa4e70f3e823b6520'}
    url_base_cats = 'http://127.0.0.1:8000/api-v1/cats/'

    def test_get_cats(self):
        resposta = requests.get(url=self.url_base_cats)
        assert resposta.status_code == 200

    def test_get_cat(self):
        resposta = requests.get(url=f'{self.url_base_cats}1/')
        assert resposta.status_code == 200

    def test_post_cat(self):
        cria_gato = {
            "breed": "Siamês Post Test",
            "location_origin": "SP",
            "coat_length": "1.35",
            "body_type": "Cobby",
            "pattern": "Gato Test Post"
        }
        resposta = requests.post(url=self.url_base_cats, headers=self.headers, data=cria_gato)
        assert resposta.status_code == 201
        assert resposta.json()['breed'] == cria_gato['breed']
        assert resposta.json()['location_origin'] == cria_gato['location_origin']
        assert resposta.json()['coat_length'] == cria_gato['coat_length']
        assert resposta.json()['body_type'] == cria_gato['body_type']
        assert resposta.json()['pattern'] == cria_gato['pattern']

    def test_put_cat(self):
        atualizar_gato = {
            "breed": "Siamês Put Test",
            "location_origin": "AC",
            "coat_length": "0.95",
            "body_type": "Cobby",
            "pattern": "Gato Test Put"
        }
        resposta = requests.put(url=f'{self.url_base_cats}1/', headers=self.headers, data=atualizar_gato)
        assert resposta.status_code == 200
        assert resposta.json()['breed'] == atualizar_gato['breed']
        assert resposta.json()['location_origin'] == atualizar_gato['location_origin']
        assert resposta.json()['coat_length'] == atualizar_gato['coat_length']
        assert resposta.json()['body_type'] == atualizar_gato['body_type']
        assert resposta.json()['pattern'] == atualizar_gato['pattern']

    def test_patch_cat(self):
        atualizar_raca = {
            "breed": "Siamês Patch Test",
        }
        resposta = requests.patch(url=f'{self.url_base_cats}2/', headers=self.headers, data=atualizar_raca)
        assert resposta.status_code == 200
        assert resposta.json()['breed'] == atualizar_raca['breed']

    def test_delete_cat(self):
        resposta = requests.delete(url=f'{self.url_base_cats}3/', headers=self.headers)
        assert resposta.status_code == 204 and len(resposta.text) == 0
