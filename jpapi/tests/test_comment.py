#pylint: disable-msg=R0201,C0116

'''imports for testing'''
import pytest
import requests_mock
from requests import exceptions as err
from ..comment import Comment


mock_data = [
    {
        "postId": 1,
        "id": 1,
        "name": "id labore ex et quam laborum",
        "email": "Eliseo@gardner.biz",
        "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
    },
    {
        "postId": 1,
        "id": 2,
        "name": "quo vero reiciendis velit similique earum",
        "email": "Jayne_Kuhic@sydney.com",
        "body": "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et"
    },
    {
        "postId": 1,
        "id": 3,
        "name": "odio adipisci rerum aut animi",
        "email": "Nikita@garfield.biz",
        "body": "quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione"
    },
    {
        "postId": 1,
        "id": 4,
        "name": "alias odio sit",
        "email": "Lew@alysha.tv",
        "body": "non et atque\noccaecati deserunt quas accusantium unde odit nobis qui voluptatem\nquia voluptas consequuntur itaque dolor\net qui rerum deleniti ut occaecati"
    },
    {
        "postId": 1,
        "id": 5,
        "name": "vero eaque aliquid doloribus et culpa",
        "email": "Hayden@althea.biz",
        "body": "harum non quasi et ratione\ntempore iure ex voluptates in ratione\nharum architecto fugit inventore cupiditate\nvoluptates magni quo et"
    }
]

class TestComment():
    '''Test cases for JSON PLacement comments api'''
    def test_get_all_comment(self):
        with requests_mock.Mocker() as mock:
            mock.get('https://jsonplaceholder.typicode.com/comments', json = mock_data, status_code = 200)

            response = Comment('https://jsonplaceholder.typicode.com').get()
            assert response.json() == mock_data
            assert response.status_code == 200

    def test_get_single_comment(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                'https://jsonplaceholder.typicode.com/comments/1',
                json = mock_data[1],
                status_code = 200
            )

            response = Comment('https://jsonplaceholder.typicode.com').get(1)
            assert response.json() == mock_data[1]
            assert response.status_code == 200

    def test_get_invalid_comment(self):
        with requests_mock.Mocker() as mock:
            mock.get(
                'https://jsonplaceholder.typicode.com/comments/500',
                status_code = 404
            )

            with pytest.raises(err.HTTPError):
                response = Comment('https://jsonplaceholder.typicode.com').get(500)
                assert response.status_code == 404

    def test_add_comment(self):
        with requests_mock.Mocker() as mock:
            mock.post(
                'https://jsonplaceholder.typicode.com/comments',
                headers = {'Content-Type': 'application/json'},
                status_code = 201
            )

            response = Comment(
                'https://jsonplaceholder.typicode.com') \
                    .add(
                        1,
                        'Mock Name',
                        'Mock Title',
                        'Mock body.'
                    )
            assert response.status_code == 201

    def test_replace_comment(self):
        with requests_mock.Mocker() as mock:
            mock.put(
                'https://jsonplaceholder.typicode.com/comments/1',
                headers = {'Content-Type': 'application/json'},
                status_code = 200
            )

            response = Comment('https://jsonplaceholder.typicode.com') \
                .replace(1, 3, 'Mock Replace Title', 'user@exmaple.nil', 'Mock replace body.')
            assert response.status_code == 200

    def test_modify_comment(self):
        with requests_mock.Mocker() as mock:
            mock.patch(
                'https://jsonplaceholder.typicode.com/comments/1',
                headers = {'Content-Type': 'application/json'},
                status_code = 200
            )

            response = Comment('https://jsonplaceholder.typicode.com') \
                .modify(1, post_id = 3, email = 'user@exmaple.nil')
            assert response.status_code == 200

    def test_delete_valid_comment(self):
        with requests_mock.Mocker() as mock:
            mock.delete(
                'https://jsonplaceholder.typicode.com/comments/1',
                status_code = 200
            )

            response = Comment('https://jsonplaceholder.typicode.com').delete(1)
            assert response.status_code == 200

    def test_delete_invalid_comment(self):
        with requests_mock.Mocker() as mock:
            mock.delete(
                'https://jsonplaceholder.typicode.com/comments/500',
                status_code = 404
            )

            with pytest.raises(err.HTTPError):
                response = Comment('https://jsonplaceholder.typicode.com').delete(500)
                assert response.status_code == 404
