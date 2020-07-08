import command_class
import vk_api
import random
import keyboards
from main import vk, cursor, connection
from message_class import MessageSettings
from user_class import UserParams
import datetime
import sqlite3
import psycopg2
import traceback
import datetime

##################################                Добавить блокировку от 3 варнов 
def info():
    id = MessageSettings.id
    today = datetime.date.today()
    try:
        idAdv = MessageSettings.payload["id"]
        #cursor.execute('SELECT * FROM "Adv" WHERE id = ' + str(idAdv))
        #res = cursor.fetchone()
        cursor.execute("UPDATE Users SET name = 'null' WHERE ID_VK = " + str(idAdv))
        cursor.execute("UPDATE Users SET ischeked = 1 WHERE ID_VK = " + str(idAdv))
        cursor.execute('SELECT warn FROM Users WHERE ID_VK = ' + str(idAdv))
        vk.method("messages.send",
            {"peer_id": int(idAdv), "message": "Ваш ник был удален модератором. Вероятно, он был некорректным. \n Также вам выдано 1 предупреждение.","keyboard": keyboards.warnList, "random_id": random.randint(1, 2147483647)})
        warnCurr = int(cursor.fetchone()[0])
        warnCurr += 1
        cursor.execute('UPDATE Users SET warn = ' + str(warnCurr) + ' WHERE ID_VK = ' + str(idAdv))
        cursor.execute("UPDATE Users SET expiration = '" + str(datetime.date(today.year, today.month, today.day) + datetime.timedelta(days = 30)) + "' WHERE ID_VK = " + str(idAdv))
        connection.commit()
        print("succs")
    except Exception:
        print('Ошибка:\n', traceback.format_exc())

    try:
        # sql = "INSERT INTO Status VALUES (" + str(id) + ", 100);"
        # cursorR.execute(sql)
        # conn.commit()
        # conn.close()
        cursor.execute('SELECT * FROM users WHERE ischeked < 1 LIMIT 1')
        res = cursor.fetchone()

        if res:
            ans = "Ник §\n"
            ans += "from @id" + str(res[0])
            ans += "\n" + str(res[1])
            vk.method("messages.send",
                      {"peer_id": id, "message": str(ans), "keyboard": keyboards.GetModerNickButton(res[0]),
                       "random_id": random.randint(1, 2147483647)})
        else:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Все проверено", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        print('Ошибка:\n', traceback.format_exc())
        #conn.rollback()
        vk.method("messages.send",
            {"peer_id": id, "message": "Произошла ошибка. Модерация", "random_id": random.randint(1, 2147483647)})
    return "ok"





command = command_class.Command()




command.keys = ['']
command.desciption = ''
command.process = info
command.payload = "deletewarnnick"
