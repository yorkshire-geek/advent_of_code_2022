from utils.objectmother import ObjectMother
from utils.datawrapper import DataWrapper

class DataWrapper (DataWrapper):
    @staticmethod
    def factory(data):
        return DataWrapper(data)

    # def get_direction(self) -> str:
    #     return self.data.split(" ")[0]

    # def get_value(self) -> int:
    #     return int(self.data.split(" ")[1])


if __name__ == "__main__":

    data = ObjectMother("input.txt").return_list(DataWrapper.factory);
    print(data);







