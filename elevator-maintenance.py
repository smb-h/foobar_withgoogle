# python 2.7.13


def solution(l):
    """
    This function takes a list of versions (strings) and 
    returns the sorted list of versions in ascending order.
    """
    return sorted(l, key=lambda s: map(int, s.split('.')))

print("==================" * 3)
print("answer: ")
print(["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"])
print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
print("==================" * 3)
# 0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0
print("answer: ")
print(["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"])
print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
print("==================" * 3)
# 1.0,1.0.2,1.0.12,1.1.2,1.3.3
print("answer: ")
print(["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"])
print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
