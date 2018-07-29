'''
Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
Google group for help: https://groups.google.com/forum/?fromgroups#!forum/beautifulsoup

Install lxml for speed
Pull data from markup file
'''

# Looks like you need to install in PyCharm separately?
from bs4 import BeautifulSoup

# Initializing BS
with open("simple_site.html") as fp:
    soup = BeautifulSoup(fp, "lxml")

    # format
    print(f'Formatted:\n{soup.prettify()}')

    # tags
    tag = soup.p
    print(
        '\nTag information'
        f'\ntype: {type(tag)}'
        f'\nname: {tag.name}'
        f'\ncontents: \n{tag}'
        f'\nid={tag["id"]}'
    )
    tag["id"] = "msg2"
    print(f'Parser\'s contents after change:\n{tag}')
    del tag["id"]
    try:
        print(f'Parser\'s contents after change:\n{tag}')
        print(f'id\'s contents after change:\n{tag["id"]}')
    except KeyError:
        print('KeyError trying to read deleted tag')

    # Navigable strings
    string1 = tag.string
    print(
        f'\n{tag.name} element string type: {type(string1)}'
        f'\n{tag.name} element contents: {string1}'
    )
    # replace tag contents
    var = string1.replace_with("Some other message.")
    print(f'\n{tag.name} element contents after change: {tag}')

    # IMPORTANT - Convert string to unicode after end of usage (just like with resource.close)

    # comments
    tag = soup.h2
    print(
        '\nTag information'
        f'\ntype: {type(tag)}'
        f'\nname: {tag.name}'
        f'\ncontents: \n{tag}'
        f'\nid={tag["id"]}'
    )
    string2 = tag.contents
    print(
        f'\n{tag.name} element string type: {type(string2)}'
        f'\n{tag.name} element contents: {string2}'
    )