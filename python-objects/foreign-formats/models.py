import os
import time
from dataclasses import dataclass


@dataclass
class User:
    name: str
    password: str

    def __getstate__(self):
        state = self.__dict__.copy()
        state["timestamp"] = int(time.time())
        del state["password"]
        return state

    def __setstate__(self, state):
        def is_in_set(n: int) -> bool:
            return (
                n == 45
                or (48 <= n <= 57)
                or n == 58
                or n == 61
                or (64 <= n <= 90)
                or n == 95
                or (97 <= n <= 122)
            )

        self.__dict__.update(state)
        s = os.urandom(80).decode("ascii", errors="ignore")
        ascii_chars = [c for c in s if is_in_set(ord(c))]
        self.password = "".join(ascii_chars)
        # print(s, self.password)
        # with open("/dev/random", mode="rb") as file:
        #     self.password = file.read(8).decode("ascii", errors="ignore")
