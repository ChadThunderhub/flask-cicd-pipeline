# Code for Flask App

FIRST_NAME:str = "Wiktor"
LAST_NAME:str = "Pieprzowski"
MAIL:str = "zoltamordemuzrob@gmail.com"


def FirstName(name: str) -> str:
    return str(f"{name}")

def LastName(lastName: str) -> str:
    return str(f"{lastName}")

def Mail(mail: str) -> str:
    return str(f"{mail}")
