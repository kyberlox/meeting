from fastapi import FastAPI, Response, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

import os
import json

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def add_form_action(data):
    file = open("./static/form_action.json", "r+")
    file_content = json.load(file)
    file_content["data"].append(data)
    json.dump(file_content, file, indent=4)
    file.close()



def send_mail(html_content):
    smtp_server = os.getenv('server')
    port = 587

    server = smtplib.SMTP(smtp_server, port)
    server.starttls()

    email = "it.dpm@emk.ru"
    password = os.getenv('password')

    server.login(email, password)

    from_email = email
    to_email_1 = "gazinskii.i.v@emk.ru"
    to_email_2 = "timofeev.a.a@emk.ru"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Сообщение отправлено через форму на сайте meeting.mosckba.ru"
    message["From"] = from_email
    message["To"] = to_email_1

    part_html = MIMEText(html_content, "html")
    message.attach(part_html)

    server.sendmail(from_email, to_email_1, message.as_string())

    message["To"] = to_email_2
    server.sendmail(from_email, to_email_2, message.as_string())

    server.quit()

    return True



app = FastAPI()

app.mount("/api/static", StaticFiles(directory="static"))

@app.get("/api/", tags=["base link"], response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Сайт седьмого стёта проектировщиков</title>
        </head>
        <body>
            <h1>На данный момент сайт находится в разработке</h1>
        </body>
    </html>
    """

@app.get("/api/video{name}", tags=["video"])
async def stream_video(name : str):
    path = f"/app/static/{name}"
    file_like  = open(path, mode="rb")

    return StreamingResponse(file_like, media_type="video/mp4")

@app.post("/api/send_form", tags=["send_message"])
async def send_message(data=Body()):
    #Сохранить для статистики
    add_form_action(data)

    #Распаковать данные из json
    fio = data["fio"]
    phone = data["phone"]
    email = data["email"]
    organization = data["organization"]
    report = "С докладом" if data["report"] else "Без доклада"

    #Собрать HTML
    html_content = f"""
    <html>
    <body>
        <table>
            <tr><td>ФИО</th><td></td><strong>{fio}</strong></td></tr>
            <tr><td>Телефон</td><td><strong>{phone}</strong></td></tr>
            <tr><td>email</td><td><strong>{email}</strong></td></tr>
            <tr><td>Организация</td><td><strong>{organization}</strong></td></tr>
            <tr><td>Статус доклада</td><td><strong>{report}</strong></td></tr>
        </table>
    </body>
    </html>
    """
    #Отправить сообщение на почту
    return send_mail(html_content)


# @app.get("/api/static_video/{name}", tags=["video"])
# async def stream_video(name : str):
#     path = f"/app/static/{name}"
#     file_like  = open(path, mode="rb")

#     return StreamingResponse(file_like, media_type="video/mp4")