
class Hello:
    def __init__(self,name="Raj") -> None:
        self.name = name

    def say_hello(self):
        return f"hai {self.name}"
    
    def say_bye(self):
        return f"bye {self.name}"

def more_hello():
    return "hi"

def more_goodbye():
    return "bye"
