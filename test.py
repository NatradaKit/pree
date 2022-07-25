"""prepro"""
def main():
    """prepro"""
    grade = float(input())
    if grade < 1.00:
        print("I'm so sad.")
    elif grade < 2.00:
        grade2 = 4-grade
        print("%.2f" %(grade2))
    else:
        print("I'm so happy.")
main()