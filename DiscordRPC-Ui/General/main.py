from pypresence import Presence
import time

BASE_DIR = 'files'

time_of_tick_update = 5

client_id = None
url = None
state = None
details = None
start = None
end = None
party_size = None
party_size_max = None
but_text = None 
but_link = None

def read_from_fields():
    global url, state, details, start, end, party_size, party_size_max, but_text, but_link
    with open(f"{BASE_DIR}/BotID", "r") as f:
        url = f.read()
    with open(f"{BASE_DIR}/DataState", "r") as f:
        state = f.read()
    with open(f"{BASE_DIR}/DataDetails", "r") as f:
        details = f.read()
    try:
        with open(f"{BASE_DIR}/DataStart", "r") as f:
            start = int(f.read())
        with open(f"{BASE_DIR}/DataEnd", "r") as f:
            end = int(f.read())
    except:pass
    try:
        with open(f"{BASE_DIR}/DataParty_size", "r") as f:
            party_size = int(f.read())
        with open(f"{BASE_DIR}/DataParty_sizeMax", "r") as f:
            party_size_max = int(f.read())
    except:pass
    with open(f"{BASE_DIR}/ButText", "r") as f:
        but_text = f.read()
    with open(f"{BASE_DIR}/ButLink", "r") as f:
        but_link = f.read()

# We use URL of image of application's avatar for parse this img to UI
# (WIP) - Will be soon
def take_client_id_from_url(url):
    slashes_finded, client_id = 0, ''
    for symbol in range(len(url)):
        if url[symbol] == '/':
            slashes_finded += 1
        if slashes_finded == 4:
            client_id = client_id + url[symbol]
    return client_id[1:]
    
        
def main_function():
    global client_id
    read_from_fields()
    client_id = take_client_id_from_url(url)

    RPC = Presence(client_id, pipe=0) 
    RPC.connect()


    while True:
        
        buttons_pack = ([{"label": f"{but_text}", "url": f"{but_link}"}] if but_text != '' else None)
        party_size_pack = ([party_size, party_size_max] if party_size_max != None else None)
        state_pack = (state if state != '' else '  ')
        details_pack = (details if details != '' else '  ')
        start_pack = (start if start != None else None)
        end_pack = (end if end != None else None)
        
        RPC.update(details=details_pack,
                   state=state_pack,
                   buttons=buttons_pack,
                   party_size=party_size_pack,
                   start=start_pack ,
                   end=end_pack)
        time.sleep(time_of_tick_update)

    
