from typing import List
from functools import wraps

def decorator_with_parameters(some_flag):
    def decorator_for_function(func):
        def function_wrapper(*args,**kwargs):
            print(f"some_flag={some_flag}")
            print(f"Calling {func.__name__} with arguments {args} and key-words {kwargs}")
            return_value = func(*args,**kwargs)
            print(f"Return value = {return_value}")
            return return_value
        return function_wrapper
    return decorator_for_function

@decorator_with_parameters(some_flag=True)
def perform_action(action: str, times: int):
    print(action)
    print(times)
    for i in range(0,times):
        print(f"Performing action: {action}.")
    return f"Successfully performed '{action}' {times} times."

print(perform_action('Taking a dump', 5))

def exception_handler(target: Exception, handler=None):
    def decorator_for_function(func):
        def function_wrapper(*args,**kwargs):
            try:
                return func(*args,**kwargs)
            except Exception as e:
                if type(e) == target:
                    if handler:
                        handler(e)
                    else:
                        print('Handling caught exception')
                else:
                    print('Not handling this exception')
                    raise e
        return function_wrapper
    return decorator_for_function

@exception_handler(target=FileNotFoundError)
def func_may_throw_exception(src,dest,exception=False):
    if exception:
        raise FileNotFoundError()
    print(f'copying {src} to {dest}')

func_may_throw_exception('penis','vagina')
func_may_throw_exception('penis','vagina',exception=True)

class GitHubError(Exception):
    def __init__(self, error: str, errors: List[str], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error = error
        self.errors = errors
    
    def __str__(self):
        return super().__str__() + "\n" + f"error={self.error}" + "\n" + f"errors={','.join(self.errors)}"

def handle_github_errors(error: GitHubError):
    print(f"Github error {error}!")

@exception_handler(target=FileExistsError, handler=lambda e: print('Handling FileExistsError error'))
@exception_handler(target=GitHubError, handler=handle_github_errors)
def get_my_issues(repo: str, closed=False, exception=False):
    """more penis"""
    if exception:
        raise GitHubError(error='shit\'s fucked', errors=['you','suck','balls'])
        # raise FileExistsError()
    print(f'Getting my issues from {repo} [closed={closed}]')

get_my_issues('ADHD', closed=True, exception=True)

def functools_wrapper_dec_args(num):
    def functools_wrapper_dec(func):
        @wraps(func)
        def with_logging(*args,**kwargs):
            print('args ' + str(args))
            print('kwargs ' + str(kwargs))
            print(num)
            print("Calling " + func.__name__)
            res = func(*args,**kwargs)
            print("Result="+str(res))
            return res
        return with_logging
    return functools_wrapper_dec

@functools_wrapper_dec_args(5)
def another_func(num):
    """Penis"""
    return 5 + 5 + num

print(another_func(5))

def functools_wrapper_dec_args2(num):
    def functools_wrapper_dec(func):
        @wraps(func)
        def with_logging(*args,**kwargs):
            self = args[0]
            print('var ' + self._var)
            print('self ' + type(self).__name__)
            print('args ' + str(args[1:]))
            print('kwargs ' + str(kwargs))
            print(num)
            print("Calling " + func.__name__)
            res = func(*args,**kwargs)
            print("Result="+str(res))
            return res
        return with_logging
    return functools_wrapper_dec

class Cls1(object):

    def __init__(self):
        self._var = 'hello world'

    @functools_wrapper_dec_args2(10)
    def _inner_func(self,num):
        print(f'_inner_func do this {num}')

Cls1()._inner_func(5)