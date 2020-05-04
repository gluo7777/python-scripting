def multiply(*numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

def build_headers(**headers_to_append):
    default_headers = {'user-agent': 'macintosh'}
    default_headers.update(headers_to_append)
    return default_headers

def send_email(*recipients, **data):
    print('send_email')
    print(recipients)
    print(data)
    print(f"Sending emails to {','.join(recipients)}.")
    print("Contents of email:")
    print(data)

def spam_email(times, *recipients, **data):
    print('spam_email')
    print(times)
    print(recipients)
    print(data)
    for i in range(0,times):
        print(f'Spam attempt {i}')
        send_email(*recipients,**data)

print(multiply())
print(multiply(1,2,3,4,5))
print(build_headers())
print(build_headers(Authorization='abc123'))

send_email()
send_email('David','Jack',subject='You suck', body='Guys, you really suck!', replyTo='Don\'t bother')

def add_four(a,b,c,d):
    print(a+b+c+d)

add_four(*[1,2,3,4])

def set_env(name,value):
    print(f"{name}={value}")

set_env(**{'name':'PATH', 'value':'C:\\System32'})

spam_email(2,'David','Jack',subject='You suck', body='Guys, you really suck!', replyTo='Don\'t bother')

def http_get(url,timeout, **optional_headers):
    print(f"Making a get request against {url} [timeout={timeout}] with optional headers {optional_headers}.")

http_get('google.com',timeout=5,**{'user-agent':'dickface'})