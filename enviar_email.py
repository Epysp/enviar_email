# -*- coding: utf-8 -*-

##Criador : Epysp

#importando lib

import os
from termcolor import colored
import smtplib

#pegando users

os.system("clear")

seu_email = input(colored("Digite Seu Email: ",'red'))

#site pra gerar token https://accounts.google.com/ServiceLogin?service=accountsettings&passive=1209600&osid=1&continue=https://myaccount.google.com/apppasswords&followup=https://myaccount.google.com/apppasswords&rart=ANgoxcf1U0jaUOrLerj1TIJEjNyb8jkIMGeOO8uhW9pGgGsQM3JJDfpd4aWA3zbgIfJg4M4whdTXXiohV33h5DxLfy4gJDaSVA&authuser=0&csig=AF-SEnY2TQdFIq8PVSPs:1585801444
token = input("Digite O Token : ")

para_email = input(colored("Digite o email para quem vai enviar : ",'yellow'))

mensagem = input(colored(" Digite a Mensagem : ",'green'))

# usando lib pra enviar

server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(f"{seu_email}",f"{token}")
server.sendmail(f"{seu_email}",f"{para_email}",f"{mensagem}")
server.quit()

print(colored("Email enviado :)",'green'))
