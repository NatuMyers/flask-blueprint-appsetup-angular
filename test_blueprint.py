__author__ = 'danielqueiroz'

import pytest

import blueprint


@pytest.fixture
def client():
    return blueprint.app.test_client()


def test_urls(client):
    r = client.get('/')
    assert r.status_code == 200

    r = client.get('/hello')
    assert r.status_code == 200

    r = client.get('/world')
    assert r.status_code == 200

    # second blueprint instance
    r = client.get('/pages/hello')
    assert r.status_code == 200

    r = client.get('/pages/world')
    assert r.status_code == 200