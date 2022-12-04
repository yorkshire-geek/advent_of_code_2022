from utils.objectmother import ObjectMother
from utils.datawrapper import DataWrapper


class DataWrapper (DataWrapper):
    @staticmethod
    def factory(data):
        return DataWrapper(data)

    def get_range_1_min(self) -> int:
        return int(self.data.split("-")[0]);

    def get_range_1_max(self) -> int:
        return int(self.data.split(",")[0].split("-")[1]);

    def get_range_2_min(self) -> int:
        return int(self.data.split(",")[1].split("-")[0]);

    def get_range_2_max(self) -> int:
        return int(self.data.split(",")[1].split("-")[1]);


def is_range_contained(min1: int, max1: int, min2: int, max2: int) -> bool:
    return (min2 >= min1 and max2 <= max1) or (min1 >= min2 and max1 <= max2);


def does_range_overlap(min1: int, max1: int, min2: int, max2: int) -> bool:
    return (min2 <= min1 <= max2) or (min2 <= max1 <= max2) or (min1 <= min2 <= max1) or (min1 <= max2 <= max1)


if __name__ == "__main__":

    data = ObjectMother("input.txt").return_list(DataWrapper.factory);
    cnt_contained = 0;
    cnt_overlap = 0;
    for item in data:
        print(item)
        if is_range_contained(item.get_range_1_min(), item.get_range_1_max(), item.get_range_2_min(), item.get_range_2_max()):
            cnt_contained += 1;
        if does_range_overlap(item.get_range_1_min(), item.get_range_1_max(), item.get_range_2_min(), item.get_range_2_max()):
            cnt_overlap += 1;

    print("cnt_contained: ", cnt_contained);
    print("cnt_overlap: ", cnt_overlap);






