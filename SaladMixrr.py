import random
import math
import os

base_list = ["Laitue", "Mesclun", "Mâche", "Pousse d'épinard", "Roquette", "Fusilli/Mesclun", "Riz/Roquette",
        "Quinoa Boulgour/Roquette", "Fusili", "Riz"]
ingredients_list = ["Melon", "Ananas", "Aubergines", "Concombres", "Falafel", "Champignons", "Courgettes", "Mais", "Oignons rouges", "Poivrons",
        "Tomates cerises allongees", "Tomates cerises confites", "Edamame", "Olives vertes", "Emmental","Feta", "Fromage de chevre", "Roquefort",
        "Grana Padano", "Mozzarella", "Mozarella di Bufala", "Tomme de brebis", "Mimolette", "Oeuf Poche","Jambon blanc", "Jambon de pays", "Bacon grille",
        "Anchois", "Crevettes", "Surimi", "Saumon Fume", "Thon", "Crouton", "Graines", "Noix"]
sauce_list = ["Moutarde a l'ancienne", "Miel Moutarde", "Ranch", "Olive balsamique", "Soja", "Tomates basilic",
        "Olive citron", "Pesto", "Agrumes", "Curry Coco"]
nb_ingr = 4


def mixer (list):
    i = random.randint(0, len(list) - 1)
    return list[i]


def display(base, sauce, ingredients):
    print(
        "++++VOTRE SALADE EST PRETE+++++\nBase: ", base,
        "\nSauce: ", sauce, "\nIngredients: "
    )
    for i in ingredients:
        print("     ", i)
    return 0


def formule ():
    foo = input("Combien d'ingredients dans la salade ? (4/6): ")
    if int(foo) == 4 or int(foo) == 6:
        global nb_ingr
        nb_ingr = int(foo)
        os.system('cls')
        menu()
    else:
        print("\nMerci de choisir entre 4 ou 6 ingredients")
        formule()


def menu ():
    while True:
        os.system('cls')
        print("++++ SaladMixrr1.0 ++++\n"
            "Formule: ", nb_ingr, " ingredients\n"
            "1. Changer la quantite d'ingredients\n"
            "2. Mixer !\n"
            "3. Quitter\n"
        )
        saisie = int(input("Choisissez une option: "))
        if saisie == 1:
            return formule()
        if saisie == 2:
            os.system('cls')
            recette()
            break
        if saisie == 3:
            print("Bye !")
            return 0
        else:
            menu()


def recette ():
    base = mixer(base_list)
    ingredients = [mixer(ingredients_list)]
    sauce = [mixer(sauce_list)]
    switch = True
    while len(ingredients) < nb_ingr:
        foo = mixer(ingredients_list)
        for i in ingredients:
            if foo == i:
                switch = False
        if switch:
            ingredients.append(foo)
        else:
            switch = True
    display(base, sauce, ingredients)
    waiter()


def waiter ():
    happy = input("\nSatisfait ? Y/N/(M)enu: ")
    if (happy.upper() == "Y"):
        print("Yummy !")
        return 0
    if (happy.upper() == "N"):
        os.system('cls')
        return recette()
    if (happy.upper() == "M"):
        os.system('cls')
        return menu()
    else:
        print("Reponse invalide")
        waiter()


if __name__ == '__main__' :
    menu()
