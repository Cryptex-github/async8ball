import random
from typing import List, Tuple


__all__: Tuple[str, ...] = ("__version__", "Ball", "BallException")
__version__: str = "3.0"


class BallException(Exception):
    ...


class Ball:
    """
    Here we start the ball
    """
    
    def __init__(self) -> None:
        self.responses_list: List[str] = [
            "As I see it, yes.", 
            "Ask again later.", 
            "Better not tell you now.", 
            "Cannot predict now.", 
            "Concentrate and ask again.", 
            "Don’t count on it.", 
            "It is certain.", 
            "It is decidedly so.", 
            "Most likely.", 
            "My reply is no.", 
            "My sources say no.", 
            "Outlook not so good.", 
            "Outlook good.", 
            "Reply hazy, try again.", 
            "Signs point to yes.", 
            "Very doubtful.", 
            "Without a doubt.", 
            "Yes.", 
            "Yes – definitely.", 
            "You may rely on it.",
            "What do you think?",
            "Maybe yes maybe not"
        ]
        
    def add_response_from_file(self, filename: str) -> None:
        with open(filename, "r") as f:
            self.responses_list += f.read().split("\n")
    
    def override_response_from_file(self, filename: str) -> None:
        with open(filename, "r") as f:
            choices = f.read().split("\n")
            self.responses_list = choices
   
    def add_response(self, response: str) -> None:
        self.responses_list.append(response)
  
    def add_response_from_list(self, response_list: List[str]) -> None:
        self.responses_list += list(response_list)
   
    def response(self, question: str) -> str:
        random.seed(len(question) * random.randint(0, 10))
        return random.choice(self.responses_list)
