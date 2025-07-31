class RegularFrame:
    def __init__(self, frame_str: str):

        self.throw1 = 0
        self.throw2 = 0
        self.throw1 = self.get_throw(frame_str[0])

        if len(frame_str) > 1:
            self.throw2 = self.get_throw(frame_str[1])

    def get_throw(self, throw: str) -> int:

        if throw == "-":
            return 0

        return int(throw)





    def calc(self) -> int:
        return self.throw1 + self.throw2