from sys import argv

def formula(hours, money_per_hour, bonus):
    return int(money_per_hour) * int(hours) + int(bonus)

file_path, hours, money_per_hour, bonus = argv

print(formula(hours, money_per_hour, bonus))