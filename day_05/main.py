def setup_columns(cd : str) -> dict:
    result = {};
    columns_as_list = cd.splitlines();
    numb_of_cols = int(columns_as_list[-1].split(" ")[-1]);

    for i in range(numb_of_cols):
        result[i + 1] = [];

    for n in range(len(columns_as_list) - 1):
        line = columns_as_list[n];
        for m in range(1, numb_of_cols + 1):
            offset = m + ((m - 1) * 3)
            if offset < len(line):
                if line[offset] != " ":
                    result[m].insert(0, line[offset]);

    return result;


def parse(cmd: str):
    return int(cmd.split(" ")[1]), int(cmd.split(" ")[3]), int(cmd.split(" ")[5])


def apply_command_1(cmd: str):
    count, source, sink = parse(cmd);

    for count in range(count):
        columns[sink].append(columns[source].pop());


def apply_command_2(cmd: str):
    count, source, sink = parse(cmd);

    tmp = [];
    for count in range(count):
        tmp.append(columns[source].pop());

    tmp.reverse();

    for item in tmp:
        columns[sink].append(item);


if __name__ == "__main__":
    with open('input.txt') as file:
        data = file.read();
        columns_data = data.split("\n\n")[0];
        commands = data.split("\n\n")[1].splitlines();

    columns = setup_columns(columns_data);

    for command in commands:
        # apply_command_1(command);
        apply_command_2(command);

    ans = "";
    for n in range(1, len(columns)+1):
        ans += columns[n][-1];

    print("answer: ", ans);
