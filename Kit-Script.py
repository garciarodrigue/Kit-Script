#!/usr/bin/env python
# -*- coding: utf-8 -*-a
import os,sys,time
from colorama import Fore, Back, Style, init
init()

magenta = Fore.MAGENTA
cyan = Fore.CYAN
blanco = Fore.WHITE
verde = Fore.GREEN
azul = Fore.BLUE
rojo = Fore.RED

inf_1 = f"""
{magenta}↱{azul}▷▷▷▷▷▷▷▷▷▷▷{magenta}↰ 
{blanco}En seguridad informática,
un ataque de denegación de servicio,
llamado también ataque DoS 
(por sus siglas en inglés, Denial of Service),
es un ataque a un sistema de computadoras o red
que causa que un servicio o recurso sea inaccesible
a los usuarios legítimos
Normalmente provoca la pérdida de la conectividad
con la red por el consumo del ancho de banda de
la red de la víctima o sobrecarga de los recursos
computacionales del sistema atacado.
{magenta}↳{azul}◁◁◁◁◁◁◁◁◁◁◁{magenta}↲
"""
inf_2 = f"""
{magenta}↱{azul}▷▷▷▷▷▷▷▷▷▷▷{magenta}↰
{blanco}Si alguna vez necesitas enviar un SMS
de forma anónima, debes asegurarte de que realmente
estás enviando el mensaje desde un número
de teléfono anónimo y no desde el tuyo.

Esto no sólo es importante si te preocupa
tu privacidad, sino también por otras razones
Por ejemplo, si intentas enviar un mensaje secreto
a alguien. Si lo envías desde tu propio teléfono móvil
la persona que lo reciba podrá ver quién lo ha enviado
Para solucionar este problema, puedes utilizar esta 
herramienta de código python llamada Anonims
•NOTA
    Solo 1 msj cada {rojo}24:{cyan}hrs
{magenta}↳{azul}◁◁◁◁◁◁◁◁◁◁◁{magenta}↲
"""
inf_3 = f"""
{magenta}↱{azul}▷▷▷▷▷▷▷▷▷▷▷{magenta}↰
{blanco}El término IRC, abreviatura de
Internet Relay Chat, se refiere a un sistema
de chat que permite enviarse mensajes de texto
con otras personas (ubicadas en otros países)
casi en tiempo real a través de Internet. Para ello,
los usuarios del IRC se conectan a una
de las numerosas redes y se unen a uno o varios
de los canales que contienen una vez en ellos
tienen la opción de enviar mensajes de texto a todos los presentes o de mantener
una conversación con solo una persona en el modo
query


Es importante tener en cuenta que cada canal está
especializado en un tema concreto
y que los usuarios también tienen
la opción de crear su propio canal.
{magenta}↳{azul}◁◁◁◁◁◁◁◁◁◁◁{magenta}↲
"""

inf_4 = f"""
{magenta}↱{azul}▷▷▷▷▷▷▷▷▷▷▷{magenta}↰
{blanco}La geolocalización basada en
direcciones IP es una técnica que se usa
para calcular la ubicación geográfica de un 
dispositivo conectado a Internet, utilizando su
dirección IP.

Este mecanismo depende de que la dirección IP
del dispositivo figure en una base de datos
con su respectiva ubicación, dirección postal,
ciudad, país, región o coordenadas.
{magenta}↳{azul}◁◁◁◁◁◁◁◁◁◁◁{magenta}↲
"""
inf = print(f"""
{rojo}★{verde}◥▬{rojo}▭▭▭▭▭▭▭▭▭▭▭{verde}◳◺{rojo}✩{verde}◿◰{rojo}▭▭▭▭▭▭▭▭▭▭▭{verde}▬◤{rojo}★

{rojo}[{azul}1{rojo}]{verde} info:{blanco} XD-Dos
{rojo}[{azul}2{rojo}]{verde} info:{blanco} Anonimsj
{rojo}[{azul}3{rojo}]{verde} info:{blanco} Secret-Garden
{rojo}[{azul}4{rojo}]{verde} info:{blanco} GeoSaturnIp
""")

logo = print(f"""{magenta}
        ╭══════{azul} ☪ {magenta}══════╮
             {cyan}Kit-Script
                {rojo}by
              {cyan}T3NSHI{magenta}

        ╰══════{azul} ☪ {magenta}══════╯
""");

script = print(f"""{magenta}
____(★)______{blanco}+++◈+++{magenta}______(★)____

{rojo}[{cyan}99{rojo}]{verde} use:{blanco} XDdos
{rojo}[{cyan}98{rojo}]{verde} use:{blanco} Anonimsj
{rojo}[{cyan}97{rojo}]{verde} use:{blanco} Secret-Garden
{rojo}[{cyan}96{rojo}]{verde} use:{blanco} GeoSaturnIp

{rojo}[{cyan}0{rojo}]{verde} use:{rojo} salir
{magenta}
____(★)______{blanco}+++◈+++{magenta}______(★)____
""");


#eleccion
def eleccion():
    try:
        elec = int(input(f"{rojo}[+]{cyan}Selecciona un num de opcion:{verde} "))
        if elec == 1:
            os.system("clear")
            print(inf_1)
            os.system("python Kit-Script.py")
        if elec == 2:
            os.system("clear")
            print(inf_2)
            os.system("python Kit-Script.py")
        if elec == 3:
            os.system("clear")
            print(inf_3)
            os.system("python Kit-Script.py")
        if elec == 4:
            os.system("clear")
            print(inf_4)
            os.system("python Kit-Script.py")

        if elec == 99:
            os.system("clear")
            print(f"{verde}DESCARGANDO SCRIPT....{blanco}")
            time.sleep(1.5)
            os.system("cd scripts ; git clone https://github.com/garciarodrigue/XDdos-Tcp")
            os.system("clear")
            ejecute = "cd scripts/XDdos-Tcp ; python Key.py"
            os.system(ejecute)
            #time.sleep(2.5)

        if elec == 98:
            os.system("clear")
            print(f"{verde}DESCARGANDO SCRIPT....{blanco}")
            time.sleep(1.5)
            os.system("cd scripts ; git clone https://github.com/garciarodrigue/Anonimsj")
            os.system("clear")
            ejecute = "cd scripts/Anonimsj ; python Key.py"
            os.system(ejecute)

        if elec == 97:
            os.system("clear")
            print(f"{verde}DESCARGANDO SCRIPT....{blanco}")
            time.sleep(1.5)
            os.system("cd scripts ; git clone https://github.com/garciarodrigue/Secret-Garden")
            os.system("clear")
            ejecute = "cd scripts/Secret-Garden ; python Hack_Chat.py"
            os.system(ejecute)
        
        if elec == 96:
            os.system("clear")
            print(f"{verde}DESCARGANDO SCRIPT....{blanco}")
            time.sleep(1.5)
            os.system("cd scripts ; git clone https://github.com/garciarodrigue/GeoSaturnIp")
            os.system("clear")
            ejecute = "cd scripts/GeoSaturnIp ; python SaturIp.py"
            os.system(ejecute)

        if elec == 0:
            os.system("clear")
            print(f"{magenta}HASTA PRONTO..!!")
        else:

            print(f"\n{rojo}Eleccion Inexistente\n")
            eleccion()
    except:
        print(f"""\n{rojo}
              Eleccion no valida
""")
        eleccion()
eleccion()

