#!/usr/bin/python3
#
# wget -t 3 -O ~/discord-bot.py https://raw.githubusercontent.com/WALL-E/config/master/discord/discord-bot.py
# chmod +x discord-bot.py
#
#
import os
import sys
import subprocess

import discord

token_filename = '/home/ec2-user/token.txt'


def execute_shell(input):
    result = subprocess.run(input, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        output = result.stdout.strip()
    else:
        output = result.stderr.strip()

    return output


if not os.path.isfile(token_filename):
    print("token.txt 文件不存在。进程即将退出。")
    sys.exit()

# 读取文件内容到变量
with open(token_filename, 'r') as file:
    token = file.read().strip("\n")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('//help'):
        await message.channel.send('command: help,hello,version,restart,upgrade,who,hostname,eip,ip,df,docker ps')

    if message.content.startswith('//hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('//version'):
        await message.channel.send('Release at 2024-03-15T15:40:00!')

    if message.content.startswith('//restart'):
        await message.channel.send('Restarting!')
        client.close()
        sys.exit(0)

    if message.content.startswith('//upgrade'):
        command = """
        wget -t 3 -O ~/discord-bot.py https://raw.githubusercontent.com/WALL-E/config/master/discord/discord-bot.py;chmod +x ~/discord-bot.py;echo 'Upgrade OK'
        """
        output = execute_shell(command)
        await message.channel.send(output)

    if message.content.startswith('//who'):
        command = "who"
        output = execute_shell(command)
        await message.channel.send(output)

    if message.content.startswith('//hostname'):
        command = "hostname"
        output = execute_shell(command)
        await message.channel.send(output)

    if message.content.startswith('//eip'):
        command = "curl https://ifconfig.io"
        output = execute_shell(command)
        await message.channel.send(output)

    if message.content.startswith('//ip'):
        command = "ip route get 8.8.8.8 | grep 8.8.8.8 | cut -d' ' -f7"
        output = execute_shell(command)
        await message.channel.send(output)

    if message.content.startswith('//df'):
        command = "df -h"
        output = execute_shell(command)
        await message.channel.send(output)

    if message.content.startswith('//uptime'):
        command = "uptime"
        output = execute_shell(command)
        await message.channel.send(output)

    if message.content.startswith('//docker ps'):
        command = "docker ps"
        output = execute_shell(command)
        await message.channel.send(output)


client.run(token)
