#!/usr/bin/python3
#
# wget https://raw.githubusercontent.com/WALL-E/config/master/discord/discord-bot.py
#
import os
import sys

import discord
import subprocess

if not os.path.isfile('//home/ec2-user/token.txt'):
    print("token.txt 文件不存在。进程即将退出。")
    sys.exit()

# 读取文件内容到变量
with open('//home/ec2-user/token.txt', 'r') as file:
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

    if message.content.startswith('//hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('//who'):
        command = "who"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        print(error)

        # 将输出内容转换为字符串
        response = output.decode("utf-8")
        await message.channel.send(response)

    if message.content.startswith('//eip'):
        command = "curl https://ifconfig.io"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        print(error)

        # 将输出内容转换为字符串
        response = output.decode("utf-8")
        await message.channel.send(response)

    if message.content.startswith('//ip'):
        command = "ip route get 8.8.8.8 | grep '8.8.8.8' | cut -d' ' -f7"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        print(error)

        # 将输出内容转换为字符串
        response = output.decode("utf-8")
        await message.channel.send(response)

    if message.content.startswith('//df -h'):
        command = "df -h"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        print(error)

        # 将输出内容转换为字符串
        response = output.decode("utf-8")
        await message.channel.send(response)
   if message.content.startswith('//uptime'):
        command = "uptime"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        print(error)

        # 将输出内容转换为字符串
        response = output.decode("utf-8")
        await message.channel.send(response)

    if message.content.startswith('//docker ps'):
        command = "docker ps"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        print(error)

        # 将输出内容转换为字符串
        response = output.decode("utf-8")
        await message.channel.send(response)

client.run(token)
