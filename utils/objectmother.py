class ObjectMother:
    def __init__(self, file_name):
        self.file_name = file_name

    def return_list(self, factory_method) -> []:

        result = []
        with open(self.file_name, 'r') as input_file:
            for line in input_file:
                result.append(factory_method(line.strip()))
        input_file.close()

        return result

    def return_list_of_multi_line_objects(self, factory_method, divider: str) -> []:

        result = []
        lines = []
        with open(self.file_name, 'r') as input_file:
            for line in input_file:
                if line.startswith(divider):
                    if len(lines) > 0:
                        result.append(factory_method(lines))
                    lines = []
                lines.append(line.strip())
        if len(lines) > 0:
            result.append(factory_method(lines))

        input_file.close()

        return result

