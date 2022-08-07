
DATES: list = [

    "01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30".split(","),
    "01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31".split(","),
    "01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31".split(","),
    "01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30".split(",")

];

TOTALDAYS: int = 122;

MONTHS: list = ["Jun", "Jul", "Aug", "Sep"];

MAXNAMELEN: int = 25;

class Builder(object):

    @staticmethod
    def get_build(data: list) -> str:

        final_str: str = "";
        dates_str: str = "";

        for date_list in DATES:

            for date in date_list:

                dates_str += date + " ";

        final_str += " " * (MAXNAMELEN + 1);
        final_str += dates_str + "\n";
        final_str += " " * (MAXNAMELEN + 1);
        final_str += "_" * len(dates_str) + "\n";

        for _dict in data:

            print(_dict);

            header: str = _dict["header"];
            names: list = _dict["names"];
            dates: list = _dict["dates"];

            names_str: str = "";
            final_block_str: str = "";
            new_names: list = [];
            new_header: str = (header + "                           ")[0:MAXNAMELEN - 1];
            final_block_str += new_header + " |\n";

            for name in names:

                name = name[0:MAXNAMELEN - 5];
                name = f"    {name}                      "[0:MAXNAMELEN - 1] + " |";
                new_names.append(name);

            for new_name in new_names:

                date: str = dates[new_names.index(new_name)];

                num_dates: list = [int(date.split("-")[0]), int(date.split("-")[1])];

                num_dates_str: str = "";
                num_dates_str = "   " * (num_dates[0] - 1);
                num_dates_str += "===" * (num_dates[1] - num_dates[0]);
                num_dates_str += "   " * (TOTALDAYS - num_dates[1]);

                final_block_str += new_name + num_dates_str + "\n";

            final_str += final_block_str;

        return final_str;
