import textwrap
import unittest
import json
import objdict

from textwrap import indent
from unittest import skip
from objdict import ObjDict

from app.preparation import clean

Protein_Type = ["Beef", 
"Chicken","Pork","Bacon","Pastrami","Salami","Bologna","Prosciutto","Sausage","Pepperoni",
"Fish","Steak","Salmon", "Tilapia","Catfish","Oyster","Clam","Shrimp","Crab","Lobster",
"Egg", "Vegetarian","Veggie","Black Bean","Tofu","Vegetable","Burger","Angus","Cheese"]

Cheese_Type = ["Cheddar","American Cheese","Swiss","Provolone","Swiss","Brie","Havarti","Cheese"]

Letuce_Type = ["Romaine", "Iceberg", "Spinach","Spring Mix", "Lettuce"]

Key_Ingredient = ["Pasta","Rice", "Noodles","Avocado","Guacamole","Strawberry", "Berries"]

Key_Feature = ["Grass Fed","Cage Free","Wild"]

#Initializing the lowercase lists for comparision

protein_lowercase = []
cheese_lowercase = []
letuce_lowercase = []
ingredient_lowercase = []
feature_lowercase = []

protein_lowercase = list((map(lambda x: x.lower(), Protein_Type)))
cheese_lowercase = list((map(lambda x: x.lower(), Cheese_Type)))
letuce_lowercase = list((map(lambda x: x.lower(), Letuce_Type)))
ingredient_lowercase = list((map(lambda x: x.lower(), Key_Ingredient)))
feature_lowercase = list((map(lambda x: x.lower(), Key_Feature)))


#Custom function to handle double words in the lookups 
# To handle words like, "blean bean", "spring mix", "american cheese"
#This returns a collated set of words as needed HMS and subsequent comparison

def hms_custom_tweak(words):

    collate=[]
    black = spring = american = 0

    for word in words:
        if(word == "eggs"):
            collate.append("egg")
        if(word == "black"):
            black = 1
            continue
        if(word =="beans") and (black == 1):
            collate.append("black bean")
            continue
        if(word == "spring"):
            continue
        if(word =="mix") and (spring == 1):
            collate.append("spring mix")
            continue
        if(word == "american"):
            american = 1
            continue
        if(word =="cheese") and (american == 1):
            collate.append("american cheese")
            continue
        collate.append(word)
    return collate


#Main function to generate the structure of menu, proteins, ingredients, features for comparison
def generate_menu_structure(standardized_menu_category, menu_item, words):

    data = ObjDict()

    data.category = standardized_menu_category

    data.Item_Name_1 = "NULL"
    data.Item_Name_2 = "NULL"
    data.Item_Name_3 = "NULL"
    data.Item_Name_4 = "NULL"

    data.primary_protein = "NULL"
    data.secondary_protein = "NULL"
    data.tertiary_protein ="NULL"

    data.Cheese_Type = "NULL"
    data.Lettuce_Type = "NULL"

    data.Other_Key_Ingredient_1 = "NULL"
    data.Other_Key_Ingredient_2 = "NULL"
    data.Other_Key_Ingredient_3 = "NULL"

    data.Key_Feature_1 = "NULL"
    data.Key_Feature_2 = "NULL"
    data.Key_Feature_3 = "NULL"

    primary = 0
    secondary = 0
    tertiary =0

    Cheese_flag = 0
    Lettuce_flag = 0

    KI1_flag = 0
    KI2_flag = 0
    KI3_flag = 0

    KF1_flag = 0
    KF2_flag = 0
    KF3_flag = 0

    cleaned_menu_text = clean(menu_item)
    cleaned_menu_text_lower = cleaned_menu_text.lower()
    tokenized_text = cleaned_menu_text_lower.split()

    j= len(tokenized_text)

    if (j>=4): 
        data.Item_Name_1 = tokenized_text[0]
        data.Item_Name_2 = tokenized_text[1]
        data.Item_Name_3 = tokenized_text[2]
        data.Item_Name_4 = tokenized_text[3]
    if (j>=3):
        data.Item_Name_1 = tokenized_text[0]
        data.Item_Name_2 = tokenized_text[1]
        data.Item_Name_3 = tokenized_text[2]
    if (j>=2):
        data.Item_Name_1 = tokenized_text[0]
        data.Item_Name_2 = tokenized_text[1]
    if (j>=1):
        data.Item_Name_1 = tokenized_text[0]
    
    for w in words:
        if  w in protein_lowercase:
            if(not primary): 
                data.primary_protein = w
                primary =1
            elif(not secondary): 
                if(data.primary_protein != w):
                    data.secondary_protein = w
                    secondary =1
            elif(not tertiary):
                if((data.primary_protein != w) and (data.secondary_protein != w)):
                    data.tertiary_protein = w
                    tertiary =1
        if w in cheese_lowercase:
            if(not Cheese_flag):
                data.Cheese_Type = w
                Cheese_flag =1
        if w in letuce_lowercase:
            if(not Lettuce_flag):
                data.Lettuce_Type = w
                Lettuce_flag =1

        if w in ingredient_lowercase:
            if(not KI1_flag):
                data.Other_Key_Ingredient_1 = w
                KI1_flag =1            
            elif(not KI2_flag):
                data.Other_Key_Ingredient_2 = w
                KI2_flag =1  
            elif(not KI3_flag):
                data.Other_Key_Ingredient_3 = w
                KI3_flag =1

        if w in feature_lowercase:
            if(not KF1_flag):
                data.Key_Feature_1 = w
                KF1_flag =1
            elif(not KF2_flag):
                data.Key_Feature_2 = w
                KF2_flag =1
            elif(not KF3_flag):
                data.Key_Feature_3 = w
                KF3_flag =1

    # json_data = data.dumps(indent = 3)
    # return(json_data)
    return(data)