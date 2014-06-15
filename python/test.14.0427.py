DEFAULT_ERROR_MESSAGE = """\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Error response</title>
    </head>
    <body>
        <h1>Error response</h1>
        <p>Error code: %(code)d</p>
        <p>Message: %(message)s.</p>
        <p>Error code explanation: %(code)s - %(explain)s.</p>
    </body>
</html>
"""

class A:
    def __init__(self):
        self.name = "Class A"

    def __str__(self):
        return self.name

class B(A):
    def __init__(self):
        super().__init__()
        self.name = self.name + "->B"

def print_some(*args, **kwargs):
    print(args)

def main():
    return "OK"

if __name__ == "__main__":
    msg = main()
    print(msg)
