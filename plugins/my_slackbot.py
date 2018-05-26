#!/usr/bin/python
# -*- coding:utf-8 -*-
import random

from slackbot.bot import respond_to

from plugins.confirm_weather import ConfirmWeather


@respond_to('かわいい')
def kawaii(message):
    message.reply('知ってる')
    message.react('+1')
@respond_to('(^.*今日.*天気.*)')
def confirm_today_weather(message, something):
    weather_class = ConfirmWeather()
    weather_class.return_today_weather(message)