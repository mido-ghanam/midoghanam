import requests, json

def get_user_key(api_url, register_api_url, json_dic):
  if not all([api_url, register_api_url, json_dic]):
    print("Please provide the API URL.")
    return None
  while True:
    r = requests.get(api_url)
    if r.status_code == 201 and r.json().get("status") == "True":
      return r.json().get("user")
    else:
      try:
        r.json()
      except:
        return "Server is down right now!"
      try:
        r = requests.post(register_api_url, json=json_dic)
        if r.status_code == 201 and r.json().get("status") == "True":
          continue
      except:
        pass

def get_preferred_sentence(preferred_language, ar_sentence, en_sentence):
  if not all([preferred_language, ar_sentence, en_sentence]):
    print("Please provide all the required parameters.")
  if str(preferred_language) == "ar":
    return ar_sentence
  elif str(preferred_language) == "en":
    return en_sentence
  else:
    print("Please provide a valid language code.")

def send_users_to_server(temp, api_url, register_api_url):
  for user_id in temp:
    try:
      m = get_user_key(api_url, register_api_url, {"user_id": user_id, "username": temp[user_id]["username"], "full_name": temp[user_id]["full_name"]})
      if m == "Server is down right now!":
        return None
      del temp[user_id]
      if not temp:
        return temp
    except:
      pass
