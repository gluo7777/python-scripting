from cgitb import handler
from mimetypes import init
from pythonjsonlogger import jsonlogger
import logging
import sys
from datetime import datetime
import pythonjsonlogger

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class CustomLogger(logging.Logger):
    def __init__(self, name: str, level: any = ...) -> None:
        super().__init__(name, level)

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if isinstance(record.msg, MyException):
            log_record['args'] = record.msg.args
            for k,v in record.msg.kwargs.items():
                if k in jsonlogger.RESERVED_ATTRS:
                    log_record[f"_{k}"] = v
                else:
                    log_record[k] = v
        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname

class MyException(Exception):

    def __init__(self, message: str, *args, **kwargs) -> None:
        self.message = message
        self.args = args
        self.kwargs = kwargs
        super().__init__(message)


# formatter = jsonlogger.JsonFormatter(json_default=json_translate)
formatter = CustomJsonFormatter()
# formatter = jsonlogger.JsonFormatter()

stderr = logging.StreamHandler(sys.stderr)
stderr.setFormatter(formatter)
logger.addHandler(stderr)

# old_factory = logging.getLogRecordFactory()

# def record_factory(*args, **kwargs):
#     record = old_factory(*args, **kwargs)
#     record.custom_attribute = 0xdecafbad
#     return record

# logging.setLogRecordFactory(record_factory)

# logger.info('hello world!')
# logger.info('hello world!',extra={
#     '_name': 'william',
#     'age': 22,
#     'friends' : [
#         'Marcus',
#         'Barth'
#     ]
# })

payload = {
    '_name': 'william',
    'client_id': '123',
    'billing_account_number': '456',
    'cash': 3.50,
    'forms': [
        '01',
        '02'
    ]
}

logger.info("payload",extra=payload)

try:
    raise MyException('something went wrong',client_id='456')
except MyException as e:
    logger.exception(e, extra=payload)

print(logger.handlers)
print(handler in logger.handlers)

