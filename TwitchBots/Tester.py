import asyncio
import logging
from traceback import format_exc
import LoggingConfig
from BotAnnotations import ModOnly

logger = logging.getLogger(__name__)

def test(func):
	def wrapper(*args):
		argString = "[]"
		if args is not None:
			try:
				joined = ", ".join([repr(x) for x in args])
				argString = f"[{joined}]"
			except Exception as ex:
				logger.error(f"Failed to join args. Type: {type(args)}. Exception to follow.")
				logger.error(format_exc())
		logger.debug(f"wrapper. argc: {len(args)} args: {argString}")
		func(args)
	return wrapper

class TestBot():
	@ModOnly
	async def testMethod(self):
		logger.debug("TEST METHOD INNER")
	
	@test
	def testMethod2(self):
		logger.debug("test 2")


async def main():
	bot = TestBot()
	await bot.testMethod()
	#bot.testMethod2()

if __name__ == '__main__':
	asyncio.run(main())
