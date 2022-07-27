import logging

def calculator():
    """
    Simple caclulator: takes from usert calulation type and two numbers
    to perform the calculation on them,
    Prints result.
    """
    action = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    element1 = float(input("Podaj składnik 1. "))
    element2 = float(input("Podaj składnik 2. "))
    action_debug = ""
    res = 0
    if action == 1:
        action_debug = "Dodaję"
        res = element1 + element2
    elif action == 2:
        action_debug = "Odejmuję"
        res = element1 - element2
    elif action == 3:
        action_debug = "Mnożę" 
        res = element1 * element2
    elif action == 4: 
        action_debug = "Dzielę" 
        res = element1  / element2       
    logging.debug(f"{action_debug} {element1} i {element2}")
    print(f"Wynik to {res}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    calculator()