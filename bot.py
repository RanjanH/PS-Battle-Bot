import dotenv
import websockets
import logging as log
import os
import asyncio
import requests
import json

log.basicConfig(level=log.INFO,filename="logs.log",filemode='w',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

dotenv.load_dotenv()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

class PSClient:
    def __init__(self):
        self.wss = "wss://sim3.psim.us/showdown/websocket"
        self.uName = os.getenv("UNAME")
        self.passw = os.getenv("PASS")
        self.uri = "https://play.pokemonshowdown.com/api/login"
        self.client = None
        self.isConnected = False
        self.isLoggedIn = False
        self.battles = None

    async def sendMSG(self,room,message:list):
        msg = room + '|' + '|'.join(message)
        log.info(f'Sending Message to websocket :> {msg}')
        await self.client.send(msg)

    async def recvMSG(self):
        msg = await self.client.recv()
        #print(msg)
        log.info(f"Received message from websocket :> {msg}")
        return msg

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
            await self.sendMSG('',['/join lobby'])
            while True:
                msg = await self.recvMSG()
                print('**',msg)
        else:
            log.error(f"Could not log in\nDetails : {response.content}")

bot = PSClient()

asyncio.get_event_loop().run_until_complete(bot.connect())
asyncio.get_event_loop().run_forever()