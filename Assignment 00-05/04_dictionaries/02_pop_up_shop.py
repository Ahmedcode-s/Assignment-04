def calc_fruits():
    
    fruits = {
        "apple":1.5,
        "durian":50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    Total_cost = 0
    for one_fruit in fruits:
        price = fruits[one_fruit]
        fruits_bought = int(input(f"How many {one_fruit} you want to buy? :"))
        Total_cost += (price * fruits_bought)

    print(f"Your total amount is {Total_cost}$.")

if __name__ == '__main__':
    calc_fruits  ()