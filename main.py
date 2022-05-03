import vimeo
import argparse


def login(token, key, secret):
    '''
    API Login to Vimeo

    :return: Vimeo client object
    '''
    client = vimeo.VimeoClient(
        token=token,
        key=key,
        secret=secret
    )
    return client


def get_user(client):
    '''
    Get Vimeo Username

    :param client:
    :return: username
    '''

    # Make the request to the server for the "/me" endpoint.
    response = client.get('/me')
    # Make sure we got back a successful response.
    assert response.status_code == 200, 'Couldn\'t fetch user data'

    username = response.json().get('name')
    assert username is not None, 'Could\'nt parse user data response'

    return username


def get_video_name(client, video_id):
    '''
    Get Video Name from Video ID

    :param client:
    :param video_id:
    :return:
    '''
    response = client.get(f'/videos/{video_id}')
    assert response.status_code == 200, f'Can\'t find video {video_id}'

    video_name = response.json().get('name')
    assert video_name is not None, 'Could\'nt parse video response'

    return video_name


def post_comment(client, video_id, content):
    '''
    Post a comment on a video using Video ID

    :param client:
    :param video_id:
    :param content:
    :return:
    '''

    response = client.post(f'/videos/{video_id}/comments', data={'text': content})
    assert response.status_code == 201, 'Comment was not posted'


def get_views(client, video_id):
    '''
    Get amount of views on a video, using Video ID

    :param client:
    :param video_id:
    :return:
    '''

    response = client.get(f'/videos/{video_id}', params={"fields": "stats"})
    assert response.status_code == 200, 'Couldn\'t fetch views'
    views = response.json().get('stats', {}).get('plays')

    assert views is not None, 'Could\'nt parse views response'

    return views


def get_likes(client, video_id):
    '''
    Get amount of likes on a video, using Video ID

    :param client:
    :param video_id:
    :return:
    '''

    response = client.get(f'/videos/{video_id}/likes')
    assert response.status_code == 200, 'Could\'nt fetch likes'

    total_likes = response.json().get('total')
    assert total_likes is not None, 'Could\'nt parse likes response'

    return total_likes


def main():
    parser = argparse.ArgumentParser(description='Perform Tasks on Vimeo API')
    parser.add_argument('--video-id', type=int, default=704939412, help='A video ID')
    parser.add_argument('--token', required=True, help='Vimeo API Token')
    parser.add_argument('--key', required=True, help='Vimeo API Key')
    parser.add_argument('--secret', required=True, help='Vimeo API Secret')
    parser.add_argument('--comment', default='nice', help='Comment content to post on the video')

    args = parser.parse_args()

    client = login(
        token=args.token,
        key=args.key,
        secret=args.secret
    )

    username = get_user(client)
    print(f'Logged in successfully to user: "{username}"')

    video_name = get_video_name(client, args.video_id)
    print(f'Acting on Video ID: {args.video_id}, Title: "{video_name}"')

    post_comment(client, args.video_id, args.comment)
    print('Posted a comment successfully')

    views = get_views(client, args.video_id)
    print(f'Number of views of the video: {views}')

    total_likes = get_likes(client, args.video_id)
    print(f'Number of likes on the video: {total_likes}')


if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
