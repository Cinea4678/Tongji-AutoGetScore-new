"""

  邮件安全发送函数

  Project Tongji-AutoGetScore
  Copyright (C) 2022 Cinea Zhan. All rights reserved.
  License: GNU General Public License v3.0

"""

import requests


def sendMail(subject, to, content):
    requests.post("https://www.cinea.com.cn/mail/sendnoreply", params={
        "to": to,
        "subject": subject,
        "body": content
    })
