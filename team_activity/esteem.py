# Team Activity: Troubleshooting Functions
# CORE 1: Your program prints the introductory text as shown in the Testing
# Procedure section.
# CORE 2: Your program prints each of the ten statements and gets a response
# from the user.
# CORE 3: Your program computes the score for each response and sums all the
# scores and displays the total score.

def main():
    """
    This function prints the instructions, collects the answers, computes the
    score, and displays the score.
    """
    print_instructions()
    answers = collecting_answers()
    total_score = compute_score(answers)
    display_score(total_score)


def print_instructions():
    """
    This function prints the instructions for the Rosenberg Self-Esteem Scale.
    """
    print("\nThis program is an implementation of the Rosenberg\n"
          "Self-Esteem Scale. This program will show you ten\n"
          "statements that you could possibly apply to yourself.\n"
          "Please rate how much you agree with each of the\n"
          "statements by responding with one of these four letters:\n\n"
          "D means you strongly disagree with the statement.\n"
          "d means you disagree with the statement.\n"
          "a means you agree with the statement.\n"
          "A means you strongly agree with the statement.\n")


def collecting_answers():
    """
    It creates a list of questions, then loops through the list, asking each
    question, and appending the answer to a list.
    :return: A list of answers
    """
    answers = []
    questions_list = [
        "I feel that I am a person of worth, at least on an equal plane with"
        "others.\n Enter D, d, a, or A: ",
        "I feel that I have a number of good qualities."
        "\n Enter D, d, a, or A: ",
        "All in all, I am inclined to feel that I am a failure."
        "\n Enter D, d, a, or A: ",
        "I am able to do things as well as most other people."
        "\n Enter D, d, a, or A: ",
        "I feel I do not have much to be proud of.\n Enter D, d, a, or A: ",
        "I take a positive attitude toward myself.\n Enter D, d, a, or A: ",
        "On the whole, I am satisfied with myself.\n Enter D, d, a, or A: ",
        "I wish I could have more respect for myself.\n Enter D, d, a, or A: ",
        "I certainly feel useless at times.\n Enter D, d, a, or A: ",
        "At times I think I am no good at all.\n Enter D, d, a, or A: "
    ]

    # Looping through the list of questions, and appending the answer to a list
    for i, question in enumerate(questions_list, 1):
        answers.append(input(f"{i}. {question}"))
    return answers


def compute_score(answers):
    """
    If the answer is "D" and the question is positive, then the score is 0.
    If the answer is "d" and the question is positive, then the score is 1.
    If the answer is "a" and the question is positive, then the score is 2.
    If the answer is "A" and the question is positive, then the score is 3.
    If the answer is "D" and the question is negative, then the score is 3.
    If the answer is "d" and the question is negative, then the score is 2.
    If the answer is "a" and the question is negative, then the score is 1.
    If the answer is "A" and the question is negative, then the score is 0

    :param answers: a list of answers to the questions
    :return: The score of the test.
    """
    score = 0
    POSITIVE = (1, 2, 4, 6, 7)
    NEGATIVE = (3, 5, 8, 9, 10)

    # Looping through the list of answers, and appending the answer to a list.
    for i, answer in enumerate(answers, 1):
        if i in POSITIVE:
            if answer == "D":
                score += 0
            elif answer == "d":
                score += 1
            elif answer == "a":
                score += 2
            elif answer == "A":
                score += 3
        elif i in NEGATIVE:
            if answer == "D":
                score += 3
            elif answer == "d":
                score += 2
            elif answer == "a":
                score += 1
            elif answer == "A":
                score += 0
    return score


def display_score(total_score):
    """
    This function takes in a number and prints out a message that includes the
    number.

    :param total_score: The total score of the user's answers
    """
    print(f"\n Your Score is {total_score}")
    print("A score below 15 may indicate problematic low self-esteem.")


# If this file was executed like this:
# > python esteem.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
