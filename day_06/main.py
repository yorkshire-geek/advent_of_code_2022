def find_unique_sequence(sequence: str, buffer_size: int) -> int:
    for n in range(len(sequence)):
        buffer = sequence[n:n+buffer_size];
        buffer_as_set = set(buffer)
        if len(buffer_as_set) == buffer_size:
            return n+buffer_size;

    return -1;


if __name__ == "__main__":
    with open('input.txt') as file:
        lines = file.read().splitlines();

    for data in lines:
        print("four character: ", find_unique_sequence(data, 4));
        print("fourteen character: ", find_unique_sequence(data, 14));



