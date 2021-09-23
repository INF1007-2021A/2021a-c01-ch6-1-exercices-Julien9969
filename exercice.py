#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        liste=[]
        compteur=0
        while compteur<2:
            liste.append(input('Entrer une donné : '))
            compteur+=1

    liste.sort()

    return liste


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        mot1_list=[]
        mot2_list=[]

        mot1=input('premier mot : ')

        for letter in mot1:
            mot1_list+=letter
        
        mot1_list.sort()

        mot2=input('2e mot : ')

        for letter in mot2:
            mot2_list+=letter
 
        mot2_list.sort()
        

        if mot1_list == mot2_list:
            return True

    return False


def contains_doubles(items: list) -> bool:
    for chiffre in items:
        if items.count(chiffre)>1:
            return True


    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    moyenne=0
    meilleure_moyenne=0
    somme=0
    nombre_notes=0

    for clé in student_grades:
        
        list_notes=student_grades[clé]
        for note in list_notes:
            somme+=note
            nombre_notes+=1

        moyenne=somme/nombre_notes
        if moyenne>meilleure_moyenne:
            meilleure_moyenne=moyenne
            meilleure_etudient=[]
            meilleur_etudiant={clé : meilleure_moyenne}

    return meilleur_etudiant


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    dict_de_freq=dict()
    frequences=str()

    for lettres in sentence:
        if lettres== " ":
            continue
        
        count = sentence.count(lettres)
        if count>5:
            dict_de_freq[lettres] =sentence.count(lettres)

    sorted_dict=sorted(dict_de_freq.items(), key=lambda x: x[1], reverse=True)

    for lists in sorted_dict:
        frequences+="\n"+f"{lists[0]}{lists[1]: >10}"

    return frequences


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    print(f"les mots sont anagrams {anagrams()}")

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
