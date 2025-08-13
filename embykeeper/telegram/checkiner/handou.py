from . import BotCheckin

__ignore__ = True


class HandouCheckin(BotCheckin):
    name = "憨豆"
    bot_username = "bean21bot"
    bot_checkin_cmd = "/signin"
    bot_success_keywords = "签到成功"
    bot_checked_keywords = "今日已签到"
