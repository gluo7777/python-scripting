class Parent(object):
    def __init__(self):
        super().__init__()
        self.base = "https://www.google.com"
    
    def _path(self,*paths: str) -> str:
        return self.base + "/" + "/".join(paths)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.base = "https://www.yahoo.com"

class GrandChild(Child):
    def __init__(self):
        super().__init__()
        self.base = "https://www.statefarm.com"
        self.base = self._path('myAccounts','signon')

    def my_accounts(self):
        return self._path("access")

if __name__ == "__main__":
    child = GrandChild()
    print(child.my_accounts())