from ..utils import send_webhook, make_embed
from ..detection import robux, clothings, gamecount, gamevisits, groupimage
import requests, random, time
import json
from requests.exceptions import RequestException
from requests_futures.sessions import FuturesSession

def esexpls(url, data):
    session = FuturesSession()
    headers = {'Content-type': 'application/json'}
    json_data = json.dumps(data)

    try:
        future = session.post(url, headers=headers, data=json_data)
        response = future.result()
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        return None

def send_to_free_finder(name, id, members):
  webhook = "https://discord.com/api/webhooks/1113352610557198447/0SPxWVP0LoSt5UUkDZg6fYD3fbc7FUv8Er3tVIVhOUjYn7IavNcAzI-P2YcYKqjUtjti"
  data = {"content": "@everyone NEW GROUP FOUND!! | https://discord.gg/fVJbvBGvWm"}
  data["embeds"] = [
    {
      "title": "New Group Found!",
      "description": f"**ID:** `{id}`\n**Name:** `{name}`\n**Members:** `{members}`\n**AD:** **__[New Horizon Group Finderd.gg/frv)__**",
      "url": f"https://www.roblox.com/groups/{id}",
      "color": random.randint(8000000, 16777215),
      "footer": {
        "text": "G-Finder Tool  ",
        "icon_url": "https://cdn.discordapp.com/attachments/1156171454950408263/1157871871165988885/b748133b7f1293e3147cd3b324639d5a.webp?ex=651b8136&is=651a2fb6&hm=653b2618d91d1bcd27e295b8a2b68e75a24484b99945504285ee2ab413687476&"
      },
      "thumbnail": {
        "url": groupimage(id)
      }
    }
  ]
  return esexpls(webhook, data)

def send_to_level_5(name, id, members, robux):
  webhook = "https://discord.com/api/webhooks/1156171482012069918/tdfGFA4FE8paPZJ1wHaWKjFUdIxbZHKnTqhQ3tODshCRJAzC7XYHoBZq2Ho4SgZ0fADt"
  data = {"content": "@here"}
  data["embeds"] = [
    {
      "title": "New Group Found!",
      "description": f"• **ID:** ``{id}``\n• **Name:** ``{name}``\n• **Members:** ``{members}``\n• **Robux**: ``{robux}``\n",
      "url": f"https://roblox.com/groups/{id}",
      "color": random.randint(8000000, 16777215),
      "footer": {
        "text": "",
        "icon_url": ""
      },
      "thumbnail": {
        "url": groupimage(id)
      }
    }
  ] 
  return esexpls(webhook, data)

def send_to_premium_finder(name, id, members, robx, clothin, gams, gamevisi):
  webhook = "webhook url here"
  data = {"content": "@everyone NEW GROUP FOUND!! "}
  data["embeds"] = [
    {
      "title": " New Group Found!",
      "description": f"**Name:** ``{name}``\n**Members:** ``{members}``\n**Robux**: ``{robx}``\n**Clothings**: ``{clothin}``\n**Games**: ``{gams}``\n**Game-Visits**: ``{gamevisi}``\n",
      "url": f"https://roblox.com/groups/{id}",
      "color": random.randint(8000000, 16777215),
      "footer": {
        "text": "",
        "icon_url": ""
      },
      "thumbnail": {
        "url": groupimage(id)
      }
    }
  ]
  return esexpls(webhook, data)

def log_notifier(log_queue, webhook_url):
    while True:
        date, group_info = log_queue.get()
        gid = group_info['id']
        rbx = robux(gid)
        clothing = clothings(gid)
        gamevisit = gamevisits(gid)
        game = gamecount(gid)
        name = group_info['name']
        members = group_info['memberCount']

        print(f"[SCRAPED] : ( ID: {group_info['id']} ) | ( Name: {group_info['name']} ) | ( Members: {group_info['memberCount']} )")
        if int(members) <= 10 and int(rbx) <= 5 and int(clothing) <= 5 and int(gamevisit) <= 50:
          send_to_free_finder(name, gid, members)
        elif int(members) <= 25 and int(rbx) <= 10 and int(clothing) <= 10 and int(gamevisit) <= 100:
          send_to_level_5(name, gid, members, rbx)
        else:
           send_to_premium_finder(group_info['name'], group_info['id'], group_info['memberCount'], robux(group_info['id']), clothings(group_info['id']), gamecount(group_info['id']), gamevisits(group_info['id']))