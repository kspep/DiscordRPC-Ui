from pypresence import Presence
import time

BASE_DIR = 'files'

time_of_tick_update = 5

InfoList = None

def read_from_fields():
    global InfoList

    
    with open(f"{BASE_DIR}/InfoList.json", "r") as f:
        InfoList = eval(f.read())
    
    print(InfoList)

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
    client_id = take_client_id_from_url(InfoList['BotID'])

    RPC = Presence(client_id, pipe=0) 
    RPC.connect()

    while True:
        
        buttons_pack = []
        if InfoList['ButLink'] != '' and InfoList['ButText'] != '': buttons_pack.append({"label": f"{InfoList['ButText']}", "url": f"{InfoList['ButLink']}"})
        if InfoList['ButLink2'] != '' and InfoList['ButText2'] != '': buttons_pack.append({"label": f"{InfoList['ButText2']}", "url": f"{InfoList['ButLink2']}"})
        if buttons_pack == []: buttons_pack = None
        
        party_size_pack = ([int(InfoList['DataParty_size']), int(InfoList['DataParty_sizeMax'])] if InfoList['DataParty_sizeMax'] != '' else None)

        state_pack = (InfoList['DataState'] if InfoList['DataState'] != '' else '  ')
        details_pack = (InfoList['DataDetails'] if InfoList['DataDetails'] != '' else '  ')
        start_pack = (int(InfoList['DataStart']) if InfoList['DataStart'] != '' else None)
        end_pack = (int(InfoList['DataEnd']) if InfoList['DataEnd'] != '' else None)
        
        RPC.update(details=details_pack,
                   state=state_pack,
                   buttons=buttons_pack,
                   party_size=party_size_pack,
                   start=start_pack ,
                   end=end_pack)
        time.sleep(time_of_tick_update)

    
