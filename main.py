import reader as rd
from block import Block
from builder import Builder

r = rd.Reader();
blocks: list = [];
all_data: list = [];

data: list = r.get_file_data("plan1");
headers: list  = r.get_headers(data);
items: list = r.get_items(data, headers);
names: list = r.get_names(items);
dates: list = r.get_dates(items);

for header in headers:

    items: list = r.get_items(data, [header]);
    names: list = r.get_names(items);
    dates: list = r.get_dates(items);

    blocks.append(Block(header, names, dates));

for block in blocks:

    data: dict = block.get_dict();
    all_data.append(data);

bld: Builder = Builder();

final_str: str = bld.get_build(all_data);

with open("out.txt", "a+") as file:

    file.seek(0);
    file.truncate();
    file.seek(0);
    file.write(final_str);
