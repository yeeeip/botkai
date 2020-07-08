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
    mesg = """ 🤖Промокод «Коронавирус»: 10 бесплатных подписок на онлайн-кинотеатры и курсы, которые запустили на время карантина 👍🏻 

Чтобы поддержать людей, которые проводят время дома на карантине или самоизолируются, онлайн-кинотеатры и образовательные платформы дарят бесплатные подписки. Длительность — от нескольких недель до полугода😨. Раньше эти сервисы были платными. 

🔥 Мы собрали все актуальные промокоды в одну подборку: проведите время карантина с пользой. А главное – берегите себя! 😉 

🎬 Кино и ТВ 

🎟 ТНТ Premier на время убирает платную подписку, чтобы людям было веселее проводить время дома. Весь контент PREMIER доступен абсолютно бесплатно всей русскоязычной аудитории. Чтобы получить бесплатный доступ, надо зарегистрироваться в сервисе и обновить приложение до последней версии. 
Сайт: https://premier.one/ 

🎟 Онлайн-кинотеатр Okko с 16 марта дарит пакет подписок «Оптимум» на 14 дней бесплатно. Его можно получить, воспользовавшись чат-ботом Okkobro в Telegram или написав слово «okkobro» в личные сообщения официальной группы Okko VK. Сервис просит зрителей рассказать об отменившихся планах и приложить фото, подтверждающее факт нахождения дома. По подписке доступны 25 тысяч единиц контента. Пользователи смогут увидеть фильм «Паразиты», ставший лауреатом премии «Оскар» в этом году, четвёртый сезон сериала «Мистер Робот», лекции TED и концерты. 
Сайт: https://okko.tv/ 

🎟 Онлайн-кинотеатр ivi делает особое предложение пользователям, находящимся на карантине: один месяц доступа к подписке ivi за 1 рубль. Активировать подписку можно в период с 16 марта до 15 апреля. 
Сайт: https://www.ivi.ru/ 

👩‍💻 Курсы 

🎙 Радио Arzamas дарит до 15 апреля бесплатную подписку на новые курсы: об «Улиссе» и Антихристе, «Детскую комнату» со сказками и легендами древних городов и вообще все-все-все курсы, подкасты и аудиоматериалы, когда-либо записанные Arzamas. 

Промокод КАРАНТИН будет действовать до 15 апреля, а ввести его можно на странице https://arzamas.academy/promo в браузере на мобильном устройстве. 

🎓 Крупнейшая в мире платформа онлайн-образования COURSERA предоставила вузам стран, пострадавших от коронавируса нового типа, бесплатный доступ к курсам. 
Он будет открыт до 31 июля 2020 года. Студенты, которые начали изучать курсы до 31 июля, будут иметь доступ до 30 сентября 2020 года. 
Сайт: https://www.coursera.org/ 

🌟 Университет интернет-профессий «Нетология» открыл бесплатный доступ ко всем лекциям. По промокоду STAYHOME можно смотреть лекции по маркетингу, бизнесу, дизайну и программированию. 
Активируйте до 31 марта: 
1. Перейдите по ссылке https://is.gd/mQmaAd , войдите в свой аккаунт или зарегистрируйтесь 
2. Выберите любой курс, нажмите кнопку «Купить» и введите в поле для промокода STAYHOME . Надпись на кнопке должна поменяться на «Начать обучение». 
3. Нажмите эту на кнопку и все курсы библиотеки станут доступны для просмотра. 

💡 Фоксфорд— онлайн-школа для учеников 1−11 классов, учителей и родителей. На онлайн-курсах и индивидуальных занятиях с репетитором школьники готовятся к ЕГЭ, ОГЭ, олимпиадам, изучают школьные предметы. Занятия ведут преподаватели МГУ, МФТИ, ВШЭ и других ведущих вузов страны. 
Фоксфорд даёт бесплатный доступ ко всем курсам по школьной программе на время карантина: https://help.foxford.ru/. 

📚 Образовательный сайт twinkl в период коронавируса дарит бесплатный доступ к материалам на месяц. Чтобы зарегистрировать промокод, нужно зайти на www.twinkl.co.uk/offer и ввести RUSTWINKLHELPS. 

✏Онлайн-курсы GeekBrains можно будет пройти бесплатно в период карантина. Каждый пользователь может выбрать три курса по направлениям: программирование, дизайн, управление и маркетинг. 

Чтобы активировать доступ, необходимо заполнить анкету на странице https://geekbrains.typeform.com/to/trMVF…, указать выбранные курсы и оставить адрес почты, на которую зарегистрирован аккаунт. 
"""
    mesg2 = """🎧 Музыка 

🎷 Венская опера начинает онлайн-трансляции своих спектаклей. https://www.wiener-staatsoper.at/en/staa… 

🎹 3апись на сайте Берлинской филармонии: «Филармония закрыта, поэтому мы идём к вам». До 31 марта по промокоду 
предоставляется бесплатный доступ ко всем архивным концертам. https://www.berliner-philharmoniker.de/ 

🎻 Баварская опера тоже даёт бесплатный доступ к своим спектаклям. Например, уже сейчас можно послушать и посмотреть Трубадура с потрясающим тенором Йонасом Кауфманом: https://www.staatsoper.de/en/news/online… 

🎭Театр 

Александринский театр покажет некоторые свои спектакли онлайн — на сайте и в пабликах театра в соцсетях. 
17 и 18 марта спектакль Жени Беркович по пьесе Ивана Вырыпаева «Солнечная линия» на Новой сцене будет синхронно транслироваться на сайте и в группе театра ВК. Кстати, на сайте Александринского театра, в официальной группе театра ВКонтакте и на Youtube-канале театра выложен познавательный контент: встречи, лекции, мастер-классы ведущих деятелей театра, историков, социологов. 
Сайт: https://alexandrinsky.ru/ 

Наслаждайтесь и не болейте! 

#коронавирус #великийновгород #газонмедиа #самоизоляция #промокод #карантин #акции #covid19"""
    vk.method("messages.send",
                        {"peer_id": id, "message": mesg, "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
    vk.method("messages.send",
                        {"peer_id": id, "message": mesg2, "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
    
      
    return "ok"



command = command_class.Command()




command.keys = ['чем заняться', 'что делать']
command.desciption = ''
command.process = info
command.payload = "homechill"

