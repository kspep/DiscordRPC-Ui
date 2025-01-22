from pypresence import Presence
import time

BASE_DIR = 'files'

time_of_tick_update = 5

InfoList = None

def read_from_fields():
    global timeOnRunMoment
    global InfoList

    timeOnRunMoment = None
    
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


timeOnRunMoment = None
def dataTime_to_seconds(dataTime, ticking, max_):
    global timeOnRunMoment
    if timeOnRunMoment == None: timeOnRunMoment = time.time()
    dataTimeMas = '['
    for i in range(len(dataTime)):
        if dataTime[i] != ':': dataTimeMas += dataTime[i]
        else: dataTimeMas += ','
    dataTimeMas += ']'
    dataTimeMas = eval(dataTimeMas)
    time_in_sec = dataTimeMas[0]*3600 + dataTimeMas[1]*60 + dataTimeMas[2]
    if not eval(max_) and not eval(ticking):
        return [1, time_in_sec+1]
    elif eval(max_) and not eval(ticking):
        return [1, timeOnRunMoment]
    elif eval(max_) and eval(ticking):
        return [1, 9999999999]
    return [timeOnRunMoment-time_in_sec, 9999999999]
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
        print(dataTime_to_seconds(InfoList['DataTime'], InfoList['Ticking'], InfoList['Max']))
        start_pack, end_pack = dataTime_to_seconds(InfoList['DataTime'], InfoList['Ticking'], InfoList['Max'])
  #      print(dataTime_to_seconds(InfoList['DataTime'], InfoList['Ticking'], InfoList['Max']))
        RPC.update(details=details_pack,
                   state=state_pack,
                   buttons=buttons_pack,
                   party_size=party_size_pack,
                   start=start_pack ,
                   end=end_pack)
        time.sleep(time_of_tick_update)

    
