from apistar import test

from app import app, movies, MOVIE_NOT_FOUND

client = test.TestClient(app)

def test_list_movies():
    response = client.get('/')
    assert response.status_code == 200

    json_resp = response.json()
    assert len(json_resp) == 1000

    expected = {"id":1, "genre":"Crime|Drama|Thriller",
                "title":"Violette (Violette Nozière)",
                "revenue":"$48721832.31","year":2008}
    assert json_resp[0] == expected

def test_create_movie():
    data = {"genre":"Crime",
            "title":"Snatch",
            "revenue":"$250,000,000",
            "year":1996}
    
    response = client.post('/',data=data)
    assert response.status_code == 201
    assert len(movies) == 1001

    response = client.get('/1001/')
    expected = {"id":1001, "genre":"Crime",
            "title":"Snatch",
            "revenue":"$250,000,000",
            "year":1996}
    
    assert response.json() == expected

