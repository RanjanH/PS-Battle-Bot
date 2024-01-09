import dotenv
import websockets
import logging as log
import os
import asyncio
import requests
import json
import threading

from random import randint,choice
from pokedex import pokedex
from pkmn_moves import move_list

log.basicConfig(level=log.INFO,filename="logs.log",filemode='w',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

dotenv.load_dotenv()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

def listen():
    loop2 = asyncio.new_event_loop()
    asyncio.set_event_loop
    bot.p()

class PSClient:
    def __init__(self):
        self.wss = "wss://sim3.psim.us/showdown/websocket"
        self.uName = os.getenv("UNAME")
        self.passw = os.getenv("PASS")
        self.uri = "https://play.pokemonshowdown.com/api/login"
        self.client = None
        self.isConnected = False
        self.isLoggedIn = False
        self.battles = []
        self.pokemon = [{},{},{},{},{},{}]
        self.active_pkmn = [{},{}]
        self.battleStart = False
        self.inBattle = True
        self.player = 1
        self.self_switch = False
        self.turn = 1
        self.frmat = []
        self.currentBattle = ''

    def p(self):
        print("done")

    async def sendMSG(self,room,message:list):
        msg = room + '|' + '|'.join(message)
        log.info(f'Sending Message to websocket :> {msg}')
        await self.client.send(msg)

    async def recvMSG(self):
        msg = await self.client.recv()
        #print(msg)
        log.info(f"Received message from websocket :> {msg}")

        if '|updatesearch|' in msg:
            print('here')
            text = msg.replace('|updatesearch|','')
            text = json.loads(text)
            print(text,'\n',self.frmat)
            if text['games'] != None and self.frmat != []:
                print('Here')
                for i in text['games'].keys():
                    if i in self.battles:
                        continue
                    self.battles = text['games'].keys()
                print(self.battles)

        if '>battle' in msg:
            for i in self.battles:
                if i in msg:
                    self.currentBattle = i
                    break
            print('battle room code - ',self.currentBattle)


        if '|pm|' in msg:
            text = (msg.split('|pm|'))[1].split('|')
            sender = text[0][1:]
            if '/challenge ' in msg:
                #print(f'Got Challenged by {sender}')
                self.frmat.append(text[3])
                if 'random' in self.frmat[-1]:
                    #print('Accepting challenge')
                    await self.sendMSG('',['/utm null'])
                    await self.sendMSG('',[f'/accept {sender}'])
                    self.inBattle = True
                    return
                
        if self.inBattle and not self.battleStart:
            if f"|p2|{self.uName}" in msg:
                self.player = 2
            if "|start" in msg:
                self.battleStart = True

        if "|request|" in msg:
            #print(msg)
            try:
                info = msg.split('\n')[1]
                info = info.replace("|request|",'')
                info = json.loads(info)
                print(info.keys())
                await self.pkmn_info(info)

                try:
                    if info['forceSwitch'] == [True]:
                        self.self_switch = True
                        await self.switch()
                except:
                    print('AHHHHHHH')

                if info['active'][0]['moves'][0]['id'] == 'recharge':
                    await self.client.send(f"{self.currentBattle}/choose move 1")
                        
                elif "wait" in info.keys():
                    if info['wait']:
                        return
                        
            except:
                pass
        if "|switch|" in msg and not self.self_switch:
            self.opp_pkmn(msg)
        if self.battleStart:
            print('Picking Move - turn = ',self.turn)
            if f"|turn|{self.turn}" in msg:
                await self.pick_move()
            if f"|win|" in msg:
                info = msg.split("|win|")
                self.battleStart = False
                self.inBattle = False
                if self.uName in msg:
                    print("-------\n I WON \n-------")
                else:
                    print("--------\n I LOST \n--------")
                
        if '|updatechallenges|' in msg:
            print('*************************************************in')
            res = (msg.split('|updatechallenges|'))[1]
            response = json.loads(res)
            print('------------------------------\n',response)
            #return '\n**************\n'+msg
        return msg
    
    async def pick_move(self):
        self.self_switch = False
        self.turn += 1
        num = [1,2,3,4]
        for i in range(4):
            if self.active_pkmn[0]['moves'][i]['disabled']:
                num.remove(i+1)
        pick = choice(num)
        log.info(f'Sending : {self.currentBattle}|/choose move {pick}')
        await self.client.send(f'{self.currentBattle}|/choose move {pick}')
        return
    
    async def switch(self):
        num = [1,2,3,4,5,6]
        while True:
            pick = choice(num)
            if self.pokemon[pick-1]['hp'] == '0 fnt':
                num.remove(pick)
            if self.pokemon[pick - 1]['active']:
                num.remove(pick)
            else:
                break

        await self.client.send(f'{self.currentBattle}|/choose switch {pick}')

    def opp_pkmn(self,msg):
        if self.player == 1:
            info = msg.split("|switch|p2")[1]
            info = info.split(":")[1]
            info = info.split(",")[0]
            info = info.strip()
            info = info.split("|")[0]
            self.active_pkmn[1]["name"] = info
            self.active_pkmn[1]["type"] = pokedex[info.lower()]["types"]
        else:
            info = msg.split("|switch|p1")[1]
            info = info.split(":")[1]
            info = info.split(",")[0]
            info = info.strip()
            info = info.split("|")[0]
            self.active_pkmn[1]["name"] = info
            self.active_pkmn[1]["type"] = pokedex[info.lower().replace(' ','')]["types"]
        
        print(self.active_pkmn)    

    async def connect(self):
        log.info("Connecting.....")
        try:
            self.client = await websockets.connect(self.wss)
            log.info('Connected!!')
            self.isConnected = True
        except:
            log.info('CONNECTION FAILED!!')
            return
        log.info('Logging in....')
        while True:
            msg = await self.recvMSG()
            split_msg = msg.split('|')
            if split_msg[1] == 'challstr' :
                log.info("Got CHALLSTR!!")
                id,challstr = split_msg[2],split_msg[3]
                break
        if self.passw:
            response = requests.post(self.uri,data = {'act':'login','name':self.uName,'pass':self.passw,'challstr':'|'.join([id,challstr])})
        else:
            response = requests.post(self.uri,data = {'act':'getassertion','userid':self.uName,'challstr':'|'.join([id,challstr])})
        if response.status_code == 200:
            if self.passw:
                responseJSON = json.loads(response.text[1:])
                if not responseJSON['actionsuccess']:
                    log.error("Couldn't log in!")
                    return
                assertion = responseJSON.get('assertion')
            else:
                assertion = responseJSON.text

            msg = ['/trn ' + self.uName + ',0,' + assertion]
            await self.sendMSG('',msg)
            msg = await self.recvMSG()
            #print(msg)
            log.info("Successfully Logged In!")
            #await self.sendMSG('',['/join lobby'])
            while True:
                await self.recvMSG()
        else:
            log.error(f"Could not log in\nDetails : {response.content}")

    async def pkmn_info(self,msg):

        for j in range(6):
            self.pokemon[j]['name'] = msg['side']['pokemon'][j]['details'].split(',')[0]
            self.pokemon[j]['hp'] = msg['side']['pokemon'][j]['condition']
            self.pokemon[j]['active'] = msg['side']['pokemon'][j]['active']
            self.pokemon[j]['moves'] = msg['side']['pokemon'][j]['moves']
            try:
                self.pokemon[j]['type'] = pokedex[((self.pokemon[j]['name'].lower()).replace('-','')).replace(" ",'')]['types']
            except KeyError as e:
                print(((self.pokemon[j]['name'].lower()).split('-'))[0].replace(" ",''))
                self.pokemon[j]['type'] = pokedex[((self.pokemon[j]['name'].lower()).split('-'))[0].replace(" ",'')]['types']
        
        for i in self.pokemon:
            if i['active']:
                self.active_pkmn[0]['name'] = i['name']
                self.active_pkmn[0]['hp'] = i['hp']
                self.active_pkmn[0]['type'] = i['type']
                self.active_pkmn[0]['moves'] = []
                for j in range(0,4):
                    self.active_pkmn[0]['moves'].append({})
                    self.active_pkmn[0]['moves'][j]['name'] = i['moves'][j]
                    try:
                        if "active" in msg.keys():
                            self.active_pkmn[0]['moves'][j]['pp'] = msg['active'][0]['moves'][j]['pp']
                            self.active_pkmn[0]['moves'][j]['disabled'] = msg['active'][0]['moves'][j]['disabled']
                    except:
                        log.error("ACTIVE KEY NOT FOUND",exc_info = True)
                    self.active_pkmn[0]['moves'][j]['type'] = move_list[self.active_pkmn[0]['moves'][j]['name']]['type']
        
        print('******************\n',self.pokemon,'\n')
        print('********')

bot = PSClient()
#listen()

asyncio.get_event_loop().run_until_complete(bot.connect())
asyncio.get_event_loop().run_forever()