from core.requests import Request


def main():
    sessionid = ''
    user_id = sessionid.split('%')[0]

    request = Request(sessionid=sessionid)

    url_get_user_followers = f'https://i.instagram.com/api/v1/friendships/{user_id}/followers/'
    response = request.get(url=url_get_user_followers)

    url_close_friends = 'https://i.instagram.com/api/v1/friendships/{user_id}/follow/'
    for follower in response.json()['users'][0:3]:
        if not follower['pk']:
            continue

        url = url_close_friends.format(user_id=follower['pk'])
        
        response = request.post(url=url)

        if response.status_code == 200:
            print(f'Seguidor {follower["pk"]} adicionado aos Close Friends com sucesso!')
        else:
            print(f'Erro ao adicionar o seguidor {follower["pk"]}.')


if __name__ == '__main__':
    main()
