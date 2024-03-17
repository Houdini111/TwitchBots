import asyncio
import inspect
import logging
from typing import Self
from traceback import format_exc
from twitchio.ext import commands
from CustomizedBot import CustomizedBot
from AnnotationUtils import get_args, call

def ModOnly(func):
	async def wrap(*args):
		argsObj = get_args(args)
		bot = argsObj.bot()
		ctx = argsObj.ctx()
		otherArgs = argsObj.otherArgs()
		if not ctx.author.is_mod:
			#TODO: Default message if this doesn't exist?
			msg = bot.config["messages"]["insufficientPermissionsMessage"]
			msg = msg.replace("<user>", ctx.author.name)
			await ctx.reply(msg)
			return
		else:
			call(bot, ctx, *otherArgs)
	return wrap