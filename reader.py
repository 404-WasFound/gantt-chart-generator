from os import getcwd

BASEDIR:    str =   getcwd();
STARTKEY:   str =   "#start";
ENDKEY:     str =   "#end";
DATEKEY:    str =   " ; ";
ITEMKEY:    str =   "-";

class Reader(object):

    @staticmethod
    def get_file_data(filename: str) -> list:

        with open(f"{BASEDIR}\\mkpf\\{filename}.mkpf", "r") as file:

            data: list = file.read().splitlines();

        return data;


    @staticmethod
    def get_headers(data: list) -> list:

        headers: list = [];

        for line in data:

            tokens: list = line.split(" ");

            if (tokens[0] == STARTKEY):

                headers.append(tokens[1]);

        return headers;


    @staticmethod
    def get_items(data: list, headers: list) -> list:

        all_items: list = [];

        for header in headers:

            items: list = [];
            count: int = 0;
            start_index: int = 0;
            end_index: int = 0;

            for line in data:

                if STARTKEY in line:

                    tokens: list = line.split(" ");

                    if (tokens[1] == header):

                        start_index = count;

                if ENDKEY in line:

                    tokens: list = line.split(" ");

                    if (tokens[1] == header):

                        end_index = count;

                count += 1;

            for i in range(start_index + 1, end_index):

                items.append(data[i]);

            all_items.append(items);

        return all_items;


    @staticmethod
    def get_names(all_items: list) -> list:

        names: list = [];

        for items in all_items:

            for item in items:

                names.append(item.split(" ; ")[0]);

        return names;


    @staticmethod
    def get_dates(all_items: list) -> list:

        dates: list = [];

        for items in all_items:

            for item in items:

                dates.append(item.split(" ; ")[1]);

        return dates;
