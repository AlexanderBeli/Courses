import requests


response = requests.get("https://api.github.com/events?per_page=1&page=0")
print(response.json()[0]["id"])

response = requests.get("https://api.github.com/events?per_page=1&page=1")
print(response.json()[0]["id"])

response = requests.get("https://api.github.com/events?per_page=1&page=2")
print(response.json()[0]["id"])


#Другой распространенный стандарт аутентификации API — это OAuth

#Нам нужно создать приложение, которое будет иметь идентификатор 
#(app_id илиclient_id) 
#и некоторую секретную строку (app_secret или client_secret).
#У нас должен быть URL-адрес перенаправления (redirect_uri), который API будет использовать для отправки нам информации.
#В результате аутентификации мы получим код (exchange_code), который необходимо обменять на токен доступа (access_token).

# Замените следующие переменные вашим Client ID и Client Secret
CLIENT_ID = "d852d5d416325457071e"
CLIENT_SECRET = "560861b5c3aa2f9e080bbdf60f5387c5784b03d6"

# Замените значение переменной с помощью url, указанного вами
# в поле "Authorization callback URL"
REDIRECT_URI = "https://httpbin.org/anything"

def create_oauth_link():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "user",
        "response_type": "code",
    }
    endpoint = "https://github.com/login/oauth/authorize"
    response = requests.get(endpoint, params=params)
    url = response.url
    return url


def exchange_code_for_access_token(code=None):
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }
    headers = {"Accept": "application/json"}
    endpoint = "https://github.com/login/oauth/access_token"
    response = requests.post(endpoint, params=params, headers=headers).json()
    #return response["access_token"]
    return response


def print_user_info(access_token=None):
    headers = {"Authorization": f"token {access_token}"}
    endpoint = "https://api.github.com/user"
    response = requests.get(endpoint, headers=headers).json()
    name = response["name"]
    username = response["login"]
    private_repos_count = response["total_private_repos"]
    print(
        f"{name} ({username}) | private repositories: {private_repos_count}"
    )

link = create_oauth_link()
print(f"Follow the link to start the authentication with GitHub: {link}")
code = input("GitHub code: ")
access_token = exchange_code_for_access_token(code)
print(f"Exchanged code {code} и access token: {access_token}")
print_user_info(access_token=access_token)
