import requests
import json
from requests_futures.sessions import FuturesSession
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import RequestException

roblox_cookie = {".ROBLOSECURITY": "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_74A73026270054F2AAD768541D3D06B4B27188C281652CF55C8A957CC7217468E23D87B6F931D3F9D5F9DB765CAD7BCD6BB3AA20781A20D2A31D46BFE64002D6DDB07A75901CA21F363CB1F425D8659FD312DA8B9541EF6EEB1CFAD0BC5AE642AC66D7E6CDFDB8900B7282613DEE28EEE593421217A0A893062C331910B7B31A2C41219B0885FBBB257A17D1535A1A01D6C5CD62A933B66FA9CED3A3083E04AB7AF093E7B7FBE58E8E61AA740F26563F1CF243BFDDDD9DC530B93336C95202CFFD7609A95B7EC1774FD41D05BEA8CA05F7837CF1DC5E3FB9053157C5BC3AEBB4ECE7DF4C5AFB7350CF12EC2C1E0936F44F90F190B2183EAFF21665AFB15165DB1A2A9E43152C7549133139233F5E0F27424E87A14AC7492AF18B3B9042F8646E806F8731BDC258E0745619D995B56FEA62720B387AB1561EF2F70352A653E06B797BD7243B62156C9DEF83E23AE143AA10C2BD0F4798BBFA16F0C7C670306FF40C7AF8ED13000F0DEF9AD571FBD9B00B53614712F5724851856BED07A30AEAB7C77CA4DC766903C45712B3EFD94DCC158DF89143A8211BD13437FBC7331D93364AB9E34B453C639CC8673B55DA104FD16FD35222EAADCA0A2A2B5CE4D141C61F6EDCDE42421E19DD573DD25815AEEE2E456C86008D7F93C39888FD99275B792E0B4ACAE3"}
def clothings(id):
  clothings = 0
  session = FuturesSession()
  retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
  session.mount('https://', HTTPAdapter(max_retries=retries))
  try:
    check = session.get(f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorTargetId={id}&CreatorType=2&Limit=30").result()
    check = check.json()
  except RequestException as e:
    print(e)
    return 0

  def get_page(cursor=None):
      nonlocal check
      try:
        if cursor:
          url = f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorTargetId={id}&CreatorType=2&Limit=30&cursor={cursor}"
        else:
          url = f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorTargetId={id}&CreatorType=2&Limit=30"
        check = session.get(url).result().json()
      except RequestException as e:
        print(e)
        return 0
      return check

  while True:
      if "data" in check:
          clothings += len(check['data'])
      if "nextPageCursor" not in check or not check['nextPageCursor']:
          break
      else:
          check = get_page(check['nextPageCursor'])
  return clothings

def robux(id):
  # Import Local Cookie Variable
  global roblox_cookie
  session = FuturesSession()
  retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
  session.mount('https://', HTTPAdapter(max_retries=retries))
  try:
      # Send the request asynchronously and return a Future object
      future = session.get(f'https://economy.roblox.com/v1/groups/{id}/currency', cookies=roblox_cookie, timeout=5)
  except RequestException as e:
    print(e)
    return 0
  try:
    response = future.result()
    data = json.loads(response.text)
    if "robux" in data:
      robux = data.get("robux", 0)
    else:
      robux = 0
  except RequestException as e:
    print(e)
    return 0
  return robux

def gamevisits(id):
  # Create a FuturesSession object
  session = FuturesSession()
  retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
  session.mount('https://', HTTPAdapter(max_retries=retries))

  # Make the API request asynchronously
  try:
    future = session.get(f'https://games.roblox.com/v2/groups/{id}/games?accessFilter=All&sortOrder=Asc&limit=100', timeout=5)
  except RequestException as e:
    print(e)
    return 0

  # Wait for the request to complete and load the response into a dictionary
  try:
    response = future.result()
    os = json.loads(response.text)
    if "data" in os:
      data = os["data"]
    else:
      data = 0
      
  except RequestException as e:
    print(e)
    return 0

  # If there are no games, return "None"
  if not data:
    return 0
  
  # Find the total number of visits for all games
  total_visits = 0
  for game in data:
    visits = game["placeVisits"]
    total_visits += visits
  return total_visits
  
def gamecount(id):
  session = FuturesSession()
  retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
  session.mount('https://', HTTPAdapter(max_retries=retries))
  try:
      # Send the request asynchronously and return a Future object
      future = session.get(f'https://games.roblox.com/v2/groups/{id}/games?accessFilter=All&sortOrder=Asc&limit=100', timeout=5)
  except RequestException as e:
    print(e)
    return 0
  try:
    response = future.result()
    os = json.loads(response.text)
    if "data" in os:
      data = os["data"]
    else:
      data = 0
  except RequestException as e:
    print(e)
    return 0
  if not data:
    return 0
  else:
    return len(data)

def groupimage(id):
  # Create a session with retries enabled
  session = FuturesSession()
  retry = Retry(connect=3, backoff_factor=0.5, status_forcelist=[502, 503, 504])
  adapter = HTTPAdapter(max_retries=retry)
  session.mount('https://', adapter)

  # Send the request asynchronously and return a Future object
  future = session.get(f'https://thumbnails.roblox.com/v1/groups/icons?groupIds={id}&size=150x150&format=Png&isCircular=false', timeout=5)

  # Wait for the request to complete and handle any errors that may occur
  try:
    response = future.result()
    icon_url = response.json()
    if "data" in icon_url and len(icon_url["data"]) > 0:
       image = icon_url["data"][0]["imageUrl"]
    else:
       image = "https://cdn.discordapp.com/icons/1078288294707744809/7d803a2786cede6dd1b0d0fb0bc52577.png?size=1024"

  except RequestException as e:
    print(e)
    image = "https://cdn.discordapp.com/icons/1078288294707744809/7d803a2786cede6dd1b0d0fb0bc52577.png?size=1024"
  return image 