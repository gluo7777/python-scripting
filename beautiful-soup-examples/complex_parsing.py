from bs4 import BeautifulSoup

# Had to open in binary format (utf-8) to avoid UnicodeDecodeError
# This only works if file is actually in utf-8
with open("complex_site.html", "rb") as fp:
    soup = BeautifulSoup(fp, "lxml")

    # Read head
    html_head = soup.head
    print(f'Formatted Header:\n{html_head.prettify()}')

    # Links
    for a_tag in soup.find_all(name='a'):
        print(f'Link: {a_tag["href"]}')

    # Traversal (similar to JsonPath)
    html_body_first_p = soup.body.p
    print(f'\nText of first p tag in body: {html_body_first_p.text}')

    print("Iterate over direct child nodes")
    for child in soup.head.contents:
        print(f'\nChild of <head> tag: {child}')

    print("Iterate over all child nodes including nexted (recursion)")
    for child in soup.head.descendants:
        print(f'\nChild of <head> tag: {child}')

    test1_tag = soup.find(attrs={"id": "test1"})
    print("\nloop through all strings")
    for s in test1_tag.strings:
        # Canonical string representation
        print(repr(s))

    print("\nloop through all strings without extra spaces")
    for s in test1_tag.stripped_strings:
        # Canonical string representation
        print(repr(s))