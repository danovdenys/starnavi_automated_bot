from typing import Dict
import requests
import logging

logger = logging.getLogger(__name__)

class SocialNetworkAPI:
    base_url: str = 'http://192.168.0.100:8000/api/'
    register_url: str = base_url + 'core/users/'
    login_url: str = base_url + 'core/login/'
    create_post_url: str = base_url + 'posting/posts/'
    like_post_url: str = base_url + 'posting/posts/%d/like/'

    @classmethod
    def register(cls, data: dict, **kwargs) -> Dict[str, str]:
        response = requests.post(cls.register_url, json=data)
        if response.status_code != 201:
            raise ValueError(response.json())
        
        user = response.json()
        logger.info(f'User {user["id"]} is registered with username {user["username"]}')
        return user
    
    @classmethod
    def login(cls, data: dict, **kwargs):
        return requests.post(cls.login_url, json=data).json()

    @classmethod
    def create_post(cls, data: dict, token: str, **kwargs) -> Dict[str, str]:
        headers = {'Authorization': f'Token {token}'}
        res = requests.post(cls.create_post_url, json=data, headers=headers)
        if res.status_code != 201:
            raise ValueError(res.json())
        post = res.json()
        logger.info(f'Post {post["id"]} is created with title {post["title"]}')
        return post

    @classmethod
    def like_post(cls, data: dict, token: str, post_id, **kwargs) -> bool:
        headers = {'Authorization': f'Token {token}'}
        url = cls.like_post_url % post_id
        logger.info(f'Post {post_id} is liked')
        return requests.post(url, json=data, headers=headers).status_code == 200
    