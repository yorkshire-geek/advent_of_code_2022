def get_priority(code : str) -> int:
    priority = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    return priority.index(code);

def get_intersection(string1 : str, string2 : str, string3 : str) -> str:
    return (set(string1) & set(string2) & set(string3)).pop();
    # return "a"

class Rucksack:
  
  def __init__(self, data : str):
    self._compartment_1 = data[:len(data)//2];
    self._compartment_2 = data[len(data)//2:];
    
  def get_compartment_1(self) -> str:
    return self._compartment_1;

  def get_compartment_2(self) -> str:
    return self._compartment_2;

  def get_intersection(self) -> str:
    return set(self._compartment_1).intersection(set(self._compartment_2)).pop();


if __name__ == "__main__":
    with open('input.txt') as file:
        rucksacks = file.read().splitlines();

# ans = 0;
# for rucksack in rucksacks:
#     ans += get_priority(Rucksack(rucksack).get_intersection());
# print("answer 1: ", ans);

ans2 = 0
for x in range(0, len(rucksacks), 3):
    # print(rucksacks[x:x+3]);
    ans2 += get_priority(get_intersection(rucksacks[x], rucksacks[x+1], rucksacks[x+2]));
    # print("---")
print("answer 2: ", ans2);