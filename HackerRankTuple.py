# this is a tuple question from hackerRank and how to solve this question in python 3 .
if __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())
    tuple_list = tuple(integer_list)
    print(hash(tuple_list))
  