from collections import Counter
from data_retriever import get_puzzle_input

def parse_input(content):
    first_column, second_column = zip(*(map(int, line.split()) for line in content.strip().split('\n')))
    return list(first_column), list(second_column)


def calculate_total_distance(left_list, right_list):
    return sum(abs(left - right) for left, right in zip(sorted(left_list), sorted(right_list)))


def calculate_similarity_score(left_list, right_list):
    right_count = Counter(right_list)

    return sum(num * right_count[num] for num in left_list)


if __name__ == "__main__":
    content = get_puzzle_input('puzzle_input.txt')
    left_list, right_list = parse_input(content)

    total_distance = calculate_total_distance(left_list, right_list)
    print(f"Total distance: {total_distance}")

    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"Similarity score: {similarity_score}")
