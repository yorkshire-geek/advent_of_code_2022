from collections import defaultdict

directory_stack = []
dirs = defaultdict(list)
files = defaultdict(list)
dirs_with_sizes = defaultdict(int)


class FileDto:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def __repr__(self):
        return self.name + " [" + str(self.size) + "]"

    def get_size(self):
        return self.size


def setup_commands() -> []:
    result = []

    with open('input.txt') as file:
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

    match cmd_ip[1]:
        case "cd":
            process_cd_command(cmd_ip)
        case "ls":
            process_ls_command(cmd_op)
        case _:
            print("Command not found:", cmd_ip, cmd_op)


def process_cd_command(inputs) -> None:
    global directory_stack
    directory = inputs[2];
    if directory == "..":
        directory_stack.pop()
    else:
        directory_stack.append(directory);


def process_ls_command(inputs) -> None:
    for line in inputs:
        type_or_size = line.split(" ")[0]
        name = line.split(" ")[1]

        if type_or_size == "dir":
            dirs[directory_stack[-1]].append(name)
        else:
            files[directory_stack[-1]].append(FileDto(name, int(type_or_size)))


def calculate_size_of_directory(input_directory: str):
    # print(input_directory)
    if input_directory in dirs_with_sizes:
        return dirs_with_sizes[input_directory]

    result = 0;
    for file in files[input_directory]:
        result += file.get_size()

    for sub_dir in dirs[input_directory]:
        result += calculate_size_of_directory(sub_dir)

    dirs_with_sizes[input_directory] = result

    return result;


def get_all_directories() -> set:
    result = set()
    for directory in dirs:
        result.add(directory)
        for sub_dir in dirs[directory]:
            result.add(sub_dir)

    return result


def show_answer() -> int:
    result = 0;
    for directory in get_all_directories():
        size = calculate_size_of_directory(directory)
        print("directory: ", directory, size)
        if size < 100000:
            result += size

    return result


if __name__ == "__main__":
    commands = setup_commands()
    for cmd in commands:
        process_command(cmd)

    print(dirs)
    print(files)
    print(get_all_directories())
    print(dirs_with_sizes)
    print("answer:", show_answer())


