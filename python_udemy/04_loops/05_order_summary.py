names = ["pradnya", "madhavi", "sam", "ali"]
bills = [50, 55, 80, 70]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees.")

# def generate_score_report(names: list[str], scores: list[int]) -> list[str]:
#     # Write your code below this line
#     std_names = ["pradnya", "sam", "ali", "madhavi"]
#     scores = [80, 75, 90, 88]
    
#     for name, marks in zip(std_names, scores):
#         print(f"{name} scored {marks} marks")
#     pass