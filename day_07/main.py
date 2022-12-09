global current_directory
= "root"

def setup_commands() -> [] :
    result = []

    with open('input_test.txt') as file:
        lines = file.read().splitlines();

    for line in lines:
        if line.startswith("$"):
            command = [];
            result.append(command);
        command.append(line);

    return result;


def process_command(cmd_data: []):
    cmd_ip = cmd_data[0].split(" ");
    cmd_op = cmd_data[1:];
    # print("cmd_ip", cmd_ip);
    # cmd_params = cmd_data[0].split(" ")[2];
    # print("cmd_params", cmd_params);
    # print("cmd_op", cmd_op);

    match cmd_ip[1]:
        case "cd":
            process_cd_command(cmd_ip)
            # print("CD FOUND:", cmd_ip);
        case _:
            print(cmd_ip)


def process_cd_command(inputs) -> None :
    # directories[""]
    directory = inputs[2];
    if dir == "..":
        print("move up")
    else:
        print("move into:", directory)
        global current_directory = inputs[2];


if __name__ == "__main__":
    directories = {}
    # current_directory = "root"

    commands = setup_commands()
    for cmd in commands:
        process_command(cmd)

    print(current_directory)