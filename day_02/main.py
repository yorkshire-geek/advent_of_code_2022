dict_question_one = {
         "A Y": 8,
         "B X": 1,
         "C Z": 6,
         "B Z": 9,
         "A X": 4,
         "B Y": 5,
         "A Z": 3,
         "C X": 7,
         "C Y": 2
}

dict_question_two = {
         "A Y": 4,
         "B Z": 9,
         "C Z": 7,
         "B X": 1,
         "A X": 3,
         "B Y": 5,
         "A Z": 8,
         "C X": 2,
         "C Y": 6  
}

if __name__ == "__main__":
    with open('input.txt') as file:
        lines = file.read().splitlines();

ans1 = 0;
ans2 = 0;
for line in lines:
    ans1 += dict_question_one[line]
    ans2 += dict_question_two[line]

print("Question 1: (should be 12458)", ans1)
print("Question 2: ", ans2)