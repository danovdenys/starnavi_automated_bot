import argparse
import json
import logging
import random

from api import SocialNetworkAPI
from service import generate_password, generate_username, generate_post_name

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Bot')

parser = argparse.ArgumentParser()
parser.add_argument('--filename', '-f', help='Path to the data file', default='data.json')
args = parser.parse_args()

filename = args.filename

with open(filename) as f:
    data = json.load(f)

number_of_users = data.get('number_of_users', 0)
max_posts_per_user = data.get('max_posts_per_user', 0)
max_likes_per_user = data.get('max_likes_per_user', 0)

users = []
logger.info(f'Creating {number_of_users} users...')
for i in range(number_of_users):
    user = SocialNetworkAPI.register(
            {
                'username': generate_username(), 
                'password': generate_password(),
                'email': ''
            }
        )
    users.append(user)

logger.info(f'Creating posts...')
posts = []

if not max_posts_per_user:
    logger.info('No posts to be made')
    exit()

for user in users:
    for i in range(random.randint(1, max_posts_per_user)):
        post = SocialNetworkAPI.create_post(
                {
                    'title': generate_post_name(),
                    'content' : generate_post_name(),
                }, 
                user['token']
            )
        posts.append(post)

if not max_likes_per_user:
    logger.info('No likes to be made')
    exit()

logger.info(f'Liking posts...')
for user in users:
    posts_to_like = random.sample(posts, random.randint(1, max_likes_per_user))
    for post in posts_to_like:
        post_id = post['id']
        SocialNetworkAPI.like_post({}, user['token'], post_id)