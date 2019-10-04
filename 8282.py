import asyncio
import discord
import time
import random
import datetime
import os

app = discord.Client()
token = os.environ["BOT_TOKEN"]

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("=============")

    await app.change_presence(activity=discord.Game(name="다비치 정주행",type=0))

@app.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == "@안녕":
        await message.channel.send(random.choice(["안녕","HI","안녕하세요","왔니","하이","하이여","하이염","이리오너라~","어서오너라~"]))

    if message.content == "@HI":
        await message.channel.send(random.choice(["안녕","HI","안녕하세요","왔니","하이","하이여","하이염","이리오너라~","어서오너라~"]))

    if message.content == "@안녕하세요":
        await message.channel.send(random.choice(["안녕","HI","안녕하세요","왔니","하이","하이여","하이염","이리오너라~","어서오너라~"]))

    if message.content == "@왔니":
        await message.channel.send(random.choice(["안녕","HI","안녕하세요","왔니","하이","하이여","하이염","이리오너라~","어서오너라~"]))

    if message.content == "@하이":
        await message.channel.send(random.choice(["안녕","HI","안녕하세요","왔니","하이","하이여","하이염","이리오너라~","어서오너라~"]))

    if message.content == "@하이여":
        await message.channel.send(random.choice(["안녕","HI","안녕하세요","왔니","하이","하이여","하이염","이리오너라~","어서오너라~"]))

    if message.content == "@하이염":
        await message.channel.send(random.choice(["안녕","HI","안녕하세요","왔니","하이","하이여","하이염","이리오너라~","어서오너라~"]))

    if message.content == "@이리오너라":
        await message.channel.send(random.choice(["안녕","HI","안녕하세요","왔니","하이","하이여","하이염","이리오너라~","어서오너라~"]))

    if message.content == "@어서오너라":
        await message.channel.send(random.choice(["안녕","HI","안녕하세요","왔니","하이","하이여","하이염","이리오너라~","어서오너라~"]))

    if message.content == "@도움말":
        await message.channel.send("니가 알아서 모하게?")

    if message.content == "@사이퍼즈":
        await message.channel.send("@할사람")
        
    if message.content == "@데바데":
        await message.channel.send("@할사람")

    if message.content == "@주사위":
        await message.channel.send(random.choice(["또르르, 1 입니다.","또르르, 2 입니다.","또르르, 3 입니다.","또르르, 4 입니다.","또르르, 5 입니다.","또르르, 6 입니다."]))

    if message.content == "@골라주기":
        await message.channel.send(random.choice(["1번 골라주기","2번 골라주기","3번 골라주기","4번 골라주기","5번 골라주기"]))

    if message.content == "@랜덤픽":
        await message.channel.send(random.choice(["?","로라스","휴톤","루이스","타라","트리비아","카인","레나","드렉슬러","도일","토마스","나이오비","시바포","웨슬리","스텔라","앨리셔","클레어","다이무스","이글","마를렌","샬럿","윌라드","레이튼","미쉘","린","빅터","카를로스","호타루","트릭시","히카르도","까미유","자네트","피터","아이작","레베카","엘리","마틴","브루스","미아","드니스","제레온","루시","티엔","하랑","제이","벨저","스톰쉐도우(내맘픽)","리첼","리사","릭","제키엘","탄야","캐럴","라이샌더","루드빅","멜빈","디아나","클리브","헬레나","에바","론","레오노르","시드니","테이","티모시","엘프리데","티샤"]))

    if message.content.startswith('@수장님'): #만약 메시지가 !test로 시작한다면
        embed = discord.Embed(title="클로뎃 모렐 (Claudette Morel)", description="수장님은 언제나 우리를 지켜주십니다. \n 보이지않는 모습으로 우리를 구원해주시죠", color=0x00ff00) #embed지정
        embed.set_footer(text = "#존예#여신#우리들의 언니#클로뎃 모렐") #embed에 푸터 추가
        embed.set_image(url="https://i.imgur.com/i8z2ruI.png") #embed에 이미지 추가
        await message.channel.send(embed=embed) #embed전송

    if message.content.startswith('@풍자'): #만약 메시지가 !test로 시작한다면
        embed = discord.Embed(title="풍자 (Poong-Ja/허드레웅미 친구)", description="뜨알기! \n 흐아아아~ \n 하아아아~", color=0x00ff00) #embed지정
        embed.set_footer(text = "#존예#여신#우리들의 딸기#풍자#츄츄펜") #embed에 푸터 추가
        embed.set_image(url="https://i.imgur.com/kZPAxqp.gif") #embed에 이미지 추가
        await message.channel.send(embed=embed) #embed전송
        
app.run(token)
