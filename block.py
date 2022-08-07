class Block(object):

    def __init__(self, header: str, names: list, dates: list) -> None:

        self.header: str = header;
        self.names: list = names;
        self.dates: list = dates;


    def get_dict(self) -> dict:

        data: dict = {"header": self.header, "names": self.names, "dates": self.dates};

        return data;
