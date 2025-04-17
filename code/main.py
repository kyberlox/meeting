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
    file = open("./static/form_action.json", "r")
    file_content = json.load(file)
    file.close()

    file = open("./static/form_action.json", "w")
    file_content["data"].append(dict(data))
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
    #Распаковать данные из json
    fio = data["fio"]
    phone = data["phone"]
    email = data["email"]
    organization = data["organization"]
    msg = data["msg"]
    report = "С докладом" if data["report"] else "Без доклада"

    #Сохранить для статистики
    jsn = {
        "fio" : fio,
        "phone" : phone,
        "email" : email,
        "organization" : organization,
        "report" : report,
        "msg" : msg
    }
    add_form_action(jsn)

    #Собрать HTML
    html_content = f"""
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333333;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
            font-size: 10pt;
        }
        .container {
            max-width: 600px;
            margin: 20px auto;
            background-color: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .header {
            background-color: #1e3a8a;
            color: white;
            padding: 20px;
            text-align: center;
        }
        .header h2 {
            margin: 0;
            font-size: 16px;
        }
        .content {
            padding: 30px;
        }
        .field {
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 1px solid #eeeeee;
        }
        .field-label {
            font-weight: bold;
            color: #666666;
            margin-bottom: 5px;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .field-value {
            font-size: 18px;
            color: #333333;
        }
        .footer {
            background-color: #f9f9f9;
            padding: 15px;
            text-align: center;
            font-size: 12px;
            color: #777777;
            border-top: 1px solid #eeeeee;
        }
        .footer p {
            margin: 5px 0;
        }
    </style>
    <div class="container">
    <div class="header">
    <h2>Обратная связь | https://meeting.mosckba.ru/</h2>
    </div>
    <div class="content">
    <div class="field">
    <div class="field-label">ФИО</div>
    <div class="field-value">{fio}</div>
    </div>
    <div class="field">
    <div class="field-label">Телефон</div>
    <div class="field-value">{phone}</div>
    </div>
    <div class="field">
    <div class="field-label">Email</div>
    <div class="field-value">{email}</div>
    </div>
    <div class="field">
    <div class="field-label">Организация</div>
    <div class="field-value">{organization}</div>
    </div>
    <div class="field">
    <div class="field-label">Участие с докладом</div>
    <div class="field-value">{report}</div>
    </div>
    <div class="field">
    <div class="field-label">Сообщение</div>
    <div class="field-value">{msg}</div>
    </div>
    </div>
    <div class="footer">
    <p>https://meeting.mosckba.ru/</p>
    </div>
    </div>
    """

    #Отправить сообщение на почту
    return send_mail(html_content)


# @app.get("/api/static_video/{name}", tags=["video"])
# async def stream_video(name : str):
#     path = f"/app/static/{name}"
#     file_like  = open(path, mode="rb")

#     return StreamingResponse(file_like, media_type="video/mp4")