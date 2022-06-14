from aws_lambda_powertools import Logger
from dataclasses import dataclass
from contextlib import contextmanager

@dataclass
class LambdaContext:
    function_name: str = "test"
    memory_limit_in_mb: int = 128
    invoked_function_arn: str = "arn:aws:lambda:eu-west-1:809313241:function:test"
    aws_request_id: str = "52fdfc07-2182-154f-163f-5f0f9a621d72"

class CustomLogger(Logger):
    
    @contextmanager
    def append_context(self, condition:bool = True, **additional_keys):
        if condition:
            keys_to_append = list(additional_keys.keys())
            self.append_keys(**additional_keys)
            try:
                yield
            finally:
                self.remove_keys(keys_to_append)
        else:
            yield

parent = CustomLogger(service="app")
lambda_child = CustomLogger(service="app", child=True)

@lambda_child.inject_lambda_context(clear_state=False)
def handler(event, context):
    with lambda_child.append_context(event["append"],**event):
        lambda_child.info("Collecting payment")
        child_task(0)
        child_task(1)
        child_task(2)
    lambda_child.info("finished")

def child_task(id:int=0):
    child = CustomLogger(service="app",child=True)
    with child.append_context(child_id=id):
        child.info(f"child {id} performing task")

handler({"append":True,'name':'will','age':28},LambdaContext())
handler({"append":False,'name':'will','age':28},LambdaContext())