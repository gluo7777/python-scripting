# Click (https://click.palletsprojects.com/en/7.x/bashcomplete/)

import click


@click.command('greet')
@click.option('--name', '-n', default=None, help='I gotta know who to greet, fool?')
@click.option('--times', '-t', default=1, help='How many times, fool?')
@click.argument('message')
def command1(name, times, message):
    """ Command that just prints random crap """
    out = message if name is None else 'Hello %s. %s' % (name, message)
    for x in range(0, times):
        click.echo(out)


if __name__ == "__main__":
    command1()
