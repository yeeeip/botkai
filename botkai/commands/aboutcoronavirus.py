import command_class
import vk_api
import random
import keyboards
from main import vk, uptime
from keyboards import coronavirusfull as keyboard
from message_class import MessageSettings
from user_class import UserParams
import datetime
import sqlite3
import psycopg2
import traceback


def info():
    id = MessageSettings.getId()
    mesg = """
    КНИТУ-КАИ временно переходит на дистанционный режим обучения
16.03.2020

C 17 марта по 5 апреля 2020 года включительно образовательный процесс в КНИТУ-КАИ будет осуществляться в дистанционном режиме.
С целью предотвращения распространения коронавирусной инфекции, в соответствии с рекомендациями Министерства науки и высшего образования РФ  и во исполнении приказа Министерства образования и науки от 14.03.2020 №397, на период с 17 марта по 5 апреля 2020 года включительно образовательный процесс в КНИТУ-КАИ  будет осуществляться в дистанционном режиме.
Организация обучения будет происходить с использованием систем электронного обучения на платформах «LMS Blackboard»   и «LMS MOODLE».
В период с 17 марта по 5 апреля в университете отменяются все массовые мероприятия, в том числе, научные, образовательные, спортивные, культурные и развлекательные.
Уважаемые студенты! Обращаем ваше внимание, что обучение реализуется в полном объеме в соответствии с действующим расписанием.

© kai.ru
    """
    vk.method("messages.send",
                        {"peer_id": id, "message": mesg, "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
    
      
    return "ok"



command = command_class.Command()




command.keys = ['', '']
command.desciption = ''
command.process = info
command.payload = "aboutcoronavirus"

