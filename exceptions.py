import logging


def doThis():
    raise Exception("Something")


try:
    doThis()
except Exception as e:
    logging.error("Something bad happen %s" % "what", exc_info=1)

print("can you see this")
