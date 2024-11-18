from datetime import datetime
from dataclasses import dataclass

@dataclass
class Books:
    """Books is a dataclass"""
    name : str
    author : str
    publish : datetime
date = datetime.now()
result = Books(name='English', author='Mark', publish=date)
print(result.__doc__)
