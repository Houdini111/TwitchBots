import asyncio
import inspect
import logging
from typing import Self
from traceback import format_exc
from twitchio.ext import commands
from CustomizedBot import CustomizedBot

def none_status(val: any) -> str:
	if val is None:
		return "None"
	return "Good"
	
class Args:
	def __init__(self, bot: CustomizedBot, ctx: commands.Context, otherArgs: list[any]):
		self.bot = bot
		self.ctx = ctx
		self.otherArgs = otherArgs
	
	def bot(self: Self) -> CustomizedBot:
		return self.bot
	
	def ctx(self: Self) -> commands.Context:
		return self.ctx
	
	def otherArgs(self: Self) -> list[any]:
		return self.otherArgs

def get_args(*args) -> Args:
	bot: CustomizedBot = None
	ctx: commands.Context = None
	otherArgs = []
	for arg in args:
		if isinstance(arg, CustomizedBot):
			bot = arg
		elif isinstance(arg, commands.Context):
			ctx = arg
		else: 
			otherArgs.append(arg)
	if bot is None or ctx is None:
		raise ValueError(f"bot and/or ctx was None. [bot, ctx]: [{none_status(bot)}, {none_status(ctx)}]")
	return Args(bot, ctx, otherArgs)
	
async def call(func, *args):
	if inspect.iscoroutinefunction(func):
		await func(*args)
	else:
		func(*args)
