import requests
token = 'Bearer BQC_FpSaPZfQEVrgZLqNvlzHwW6ZhB5j8Usi9Hyg3jjkK5crDCybZdNBBd75oDHjSbQ299-S7bAu54BvJtu-2t8GZcY7g3DC1oPczxg8U6YhfxtFUgKqR8lkwhd_U6S9LMiLbeYP2T-Ocw4PjQwM4GyDzwow-DrN0tF07EPqvGw4z7G4F-MPFP3b1d4_-hFglX7qNV9p_0PmzNwRPJaDmrilUsfRW2vMAk5ppXKzVvG02l5sxL9MycCOkEdOUGxym_C-sE0dMSWTRgcq8Phw3vK_jnkZi0fxCXBR2CA0pH31'
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': token,
}

params = (
    ('market', 'TR'),
    ('additional_types', 'episode'),
)

response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers, params=params)
data = response.json()
music = data['item']['name']
artist = data['item']['artists'][0]['name']


print(artist + "-" + music)