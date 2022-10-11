# Convert string into Python dictionary
from unicodedata import category
from objdict import ObjDict
from textwrap import indent
from unittest import skip
import json

Total_Menu_Section_Score = 30
Total_Menu_Item_Score = 70
Total_category_value = 0.7*Total_Menu_Item_Score
total_possible_menu_item_score = 135
TOTAL_POSSIBLE_KEY_FEATURE = 99.99
CHEESE_TYPE_MATCH_BOTH_SCORE = 15
CHEESE_TYPE_MATCH_SINGLE_SCORE = 10
LETUCE_TYPE_MATCH_BOTH_SCORE =10
LETUCE_TYPE_MATCH_SINGLE_SCORE = 7
OTHER_KEY_INGREDIENT_SCORE = 5

match_table = {'P100': {'percentage_match': 1.0,
  'name_match': 0.8,
  'ingredient_match': 0.15,
  'feature_match': 0.05},
 'P75': {'percentage_match': 0.75,
  'name_match': 0.65,
  'ingredient_match': 0.3,
  'feature_match': 0.05},
 'P50': {'percentage_match': 0.5,
  'name_match': 0.25,
  'ingredient_match': 0.7,
  'feature_match': 0.05},
 'P25': {'percentage_match': 0.25,
  'name_match': 0.25,
  'ingredient_match': 0.7,
  'feature_match': 0.05},
 'P0': {'percentage_match': 0.0,
  'name_match': 0.0,
  'ingredient_match': 0.95,
  'feature_match': 0.05}}

primary_protein_match_table = {
'match1-1': {'Primary_Protein_Code': '1-1', 'score': 55},
'match1-2': {'Primary_Protein_Code': '1-2', 'score': 30},
'match1-3': {'Primary_Protein_Code': '1-3', 'score': 15},
'match1-0': {'Primary_Protein_Code': '1-0', 'score': 0},
'match0-0': {'Primary_Protein_Code': '0-0', 'score': 0}}

secondary_protein_match_table = {
'match2-2': {'Secondary_Protein_Code': '2-2', 'score': 30},
'match2-1': {'Secondary_Protein_Code': '2-1', 'score': 30},
'match2-3': {'Secondary_Protein_Code': '2-3', 'score': 10},
'match2-0': {'Secondary_Protein_Code': '2-0', 'score': 0},
'match0-0': {'Secondary_Protein_Code': '0-0', 'score': 0}}

tertiary_protein_match_table = {
'match3-3': {'Tertiary_Protein_Code': '3-3', 'score': 10},
'match3-1': {'Tertiary_Protein_Code': '3-1', 'score': 10},
'match3-2': {'Tertiary_Protein_Code': '3-2', 'score': 5},
'match3-0': {'Tertiary_Protein_Code': '3-0', 'score': 0},
'match0-0': {'Tertiary_Protein_Code': '0-0', 'score': 0}}

def round_to_multiple(number, multiple):
    return multiple*round(number/multiple)

def compare_menus_and_score(json1_dict, json2_dict):

    item_name_count = 0

    # json1_dict = ObjDict()
    # json2_dict = ObjDict()

    # json1_dict = json.loads(json_data1)
    # json2_dict = json.loads(json_data2)

    # print(json1_dict)

    hms_standardised_menu_category = json1_dict.get('category')
    comp_standardised_menu_category = json2_dict.get('category')
    print(f"HMS Host Menu Item Category = {hms_standardised_menu_category} ")
    print(f"Comp Store Menu Item Category = {comp_standardised_menu_category} ")

    #calculation of Category Value
    if (json1_dict.get('category') != 'NULL') and (json2_dict.get('category') != 'NULL'):
        if (json1_dict.get('category') == json2_dict.get('category')):
            Category_value = Total_Menu_Section_Score
        else:
            Category_value = 0

    print(f"HMS Host Menu and Comp Store Menu Category Match - Category_value = {Category_value}")

    #calculation of Menu Item Name Value

    print(json1_dict.get('Item_Name_1'))
    print(json2_dict.get('Item_Name_1'))

    if((json1_dict.get('Item_Name_1')) != "NULL"):
        if ((json1_dict.get('Item_Name_1')) == (json2_dict.get('Item_Name_1')) or 
        (json2_dict.get('Item_Name_2')) or 
        (json2_dict.get('Item_Name_3')) or 
        (json2_dict.get('Item_Name_4'))):
            item_name_count = item_name_count + 1
            print(f"match:count - Item_Name_1 = {item_name_count}")

    print(json1_dict.get('Item_Name_2'))
    print(json2_dict.get('Item_Name_2'))

    if((json1_dict.get('Item_Name_2')) != "NULL"):
        if ((json1_dict.get('Item_Name_2')) == (json2_dict.get('Item_Name_1')) or 
        (json2_dict.get('Item_Name_2')) or 
        (json2_dict.get('Item_Name_3')) or 
        (json2_dict.get('Item_Name_4'))):
            item_name_count = item_name_count + 1
            print(f"match:count - Item_Name_2 = {item_name_count}")

    print(json1_dict.get('Item_Name_3'))
    print(json2_dict.get('Item_Name_3'))

    if((json1_dict.get('Item_Name_3')) != "NULL"):
        if ((json1_dict.get('Item_Name_3')) == (json2_dict.get('Item_Name_1')) or 
        (json2_dict.get('Item_Name_2')) or 
        (json2_dict.get('Item_Name_3')) or 
        (json2_dict.get('Item_Name_4'))):
            item_name_count = item_name_count + 1
            print(f"match:count - Item_Name_3 = {item_name_count}")

    print(json1_dict.get('Item_Name_4'))
    print(json2_dict.get('Item_Name_4'))

    if((json1_dict.get('Item_Name_4')) != "NULL"):
        if ((json1_dict.get('Item_Name_4')) == (json2_dict.get('Item_Name_1')) or 
        (json2_dict.get('Item_Name_2')) or 
        (json2_dict.get('Item_Name_3')) or 
        (json2_dict.get('Item_Name_4'))):
            item_name_count = item_name_count + 1
            print(f"match:count - Item_Name_4 = {item_name_count}")

    sum = 0
    if ((json1_dict.get('Item_Name_1')) != "NULL"):
        sum = sum+1
    if ((json1_dict.get('Item_Name_2')) != "NULL"):
        sum = sum+1
    if ((json1_dict.get('Item_Name_3')) != "NULL"):
        sum = sum+1
    if ((json1_dict.get('Item_Name_4')) != "NULL"):
        sum = sum+1
    print(f"MENU ITEM NOT NULL = {sum}")

    mround = round_to_multiple(item_name_count/sum, 0.25)
    print(mround)

    for x in match_table:
        if(match_table[x].get('percentage_match') == mround):
            name_match_weight = match_table[x].get('name_match')
            print(name_match_weight)

    Menu_Item_Name_Value = (name_match_weight)*(Total_Menu_Item_Score)

    print(f"Menu_Item_Name_Value => {Menu_Item_Name_Value}")

    #calculcation of Key Ingredient 

    sum = 0
    if ((json1_dict.get('primary_protein')) != "NULL"):
        sum = sum+1
    if ((json1_dict.get('secondary_protein')) != "NULL"):
        sum = sum+1
    if ((json1_dict.get('tertiary_protein')) != "NULL"):
        sum = sum+1
    #print(f"Protein NOT NULL = {sum}")

    count = 0
    primary_string = ""
    if((json1_dict.get('primary_protein')) != "NULL"):
        if((json1_dict.get('primary_protein')) == (json2_dict.get('primary_protein'))):
            primary_string = "1-1"
            print(f"primary_string match ==> {primary_string}")
        if((json1_dict.get('primary_protein')) == (json2_dict.get('secondary_protein'))):
            primary_string = "1-2"
            print(f"primary_string match ==> {primary_string}")
        if((json1_dict.get('primary_protein')) == (json2_dict.get('tertiary_protein'))):
            primary_string = "1-3"
            print(f"primary_string match ==> {primary_string}")
        if((json1_dict.get('primary_protein') != (json2_dict.get('primary_protein'))) and 
            (json1_dict.get('primary_protein') != (json2_dict.get('secondary_protein'))) and
            (json1_dict.get('primary_protein') != (json2_dict.get('tertiary_protein'))) 
            ):
            primary_string = "1-0"
            print(f"primary_string match ==> {primary_string}")
    else:
        primary_string = "0-0"
        print(f"primary_string match ==> {primary_string}")


    secondary_string = ""
    if((json1_dict.get('secondary_protein')) != "NULL"):
        if((json1_dict.get('secondary_protein')) == (json2_dict.get('primary_protein'))):
            secondary_string = "2-1"
            print(f"secondary_string match ==> {secondary_string}")
        if((json1_dict.get('secondary_protein')) == (json2_dict.get('secondary_protein'))):
            secondary_string = "2-2"
            print(f"secondary_string match ==> {secondary_string}")
        if((json1_dict.get('secondary_protein')) == (json2_dict.get('tertiary_protein'))):
            secondary_string = "2-3"
            print(f"secondary_string match ==> {secondary_string}")
        if((json1_dict.get('secondary_protein') != (json2_dict.get('primary_protein'))) and 
            (json1_dict.get('secondary_protein') != (json2_dict.get('secondary_protein'))) and
            (json1_dict.get('secondary_protein') != (json2_dict.get('tertiary_protein'))) 
            ):
            secondary_string = "2-0"
            print(f"secondary_string match ==> {secondary_string}")
    else:
        secondary_string = "0-0"
        print(f"secondary_string match ==> {secondary_string}")


    tertiary_string = ""
    if((json1_dict.get('tertiary_protein')) != "NULL"):
        if((json1_dict.get('tertiary_protein')) == (json2_dict.get('primary_protein'))):
            tertiary_string = "3-1"
            print(f"tertiary_string match ==> {tertiary_string}")
        if((json1_dict.get('tertiary_protein')) == (json2_dict.get('secondary_protein'))):
            tertiary_string = "3-2"
            print(f"tertiary_string match ==> {tertiary_string}")
        if((json1_dict.get('tertiary_protein')) == (json2_dict.get('tertiary_protein'))):
            tertiary_string = "3-3"
            print(f"tertiary_string match ==> {tertiary_string}")
        if((json1_dict.get('tertiary_protein') != (json2_dict.get('primary_protein'))) and 
            (json1_dict.get('tertiary_protein') != (json2_dict.get('secondary_protein'))) and
            (json1_dict.get('tertiary_protein') != (json2_dict.get('tertiary_protein'))) 
            ):
            tertiary_string = "3-0"
            print(f"tertiary_string match ==> {tertiary_string}")
    else:
        tertiary_string = "0-0"
        print(f"tertiary_string match ==> {tertiary_string}")


    for x in primary_protein_match_table:
        if(primary_protein_match_table[x].get('Primary_Protein_Code') == primary_string):
            primary_protein_match_score = primary_protein_match_table[x].get('score')
            print(f"primary_protein_match_score from table ==> {primary_protein_match_score}")
            
    for x in secondary_protein_match_table:
        if(secondary_protein_match_table[x].get('Secondary_Protein_Code') == secondary_string):
            secondary_protein_match_score = secondary_protein_match_table[x].get('score')
            print(f"secondary_protein_match_score from table ==> {secondary_protein_match_score}")

    for x in tertiary_protein_match_table:   
        if(tertiary_protein_match_table[x].get('Tertiary_Protein_Code') == tertiary_string):
            tertiary_protein_match_score = tertiary_protein_match_table[x].get('score')
            print(f"tertiary_protein_match_score from table ==> {tertiary_protein_match_score}")

    #Calculation of CheeseType
    if((json1_dict.get('Cheese_Type')) != "NULL"):
        if((json1_dict.get('Cheese_Type')) == (json2_dict.get('Cheese_Type'))):
            print(f"HMS cheese {(json1_dict.get('Cheese_Type'))} is matching with comp {(json2_dict.get('Cheese_Type'))}")
            print(f"Cheese Type match")
            cheese_type_match_score = CHEESE_TYPE_MATCH_BOTH_SCORE
        elif((json2_dict.get('CheeseType')) == "cheese"):
            cheese_type_match_score = CHEESE_TYPE_MATCH_SINGLE_SCORE
    else:
        cheese_type_match_score = 0

    print(f"cheese_type_match_score from table ==> {cheese_type_match_score}")


    #Calculation of Letuce
    if((json1_dict.get('Lettuce_Type')) != "NULL"):
        if((json1_dict.get('Lettuce_Type')) == (json2_dict.get('Lettuce_Type'))):
            print(f"HMS letuce {(json1_dict.get('Cheese_Type'))} is matching with comp {(json2_dict.get('Cheese_Type'))}")
            print(f"Letuce Type match")
            letuce_type_match_score = LETUCE_TYPE_MATCH_BOTH_SCORE
        elif((json2_dict.get('Lettuce_Type')) == "letuce"):
            letuce_type_match_score = LETUCE_TYPE_MATCH_SINGLE_SCORE
    else:
        letuce_type_match_score = 0

    print(f"letuce_type_match_score from table ==> {letuce_type_match_score}")

    #Other_key_ingredient calculations

    other_key_ingredient_1_score =0
    if((json1_dict.get('Other_Key_Ingredient_1')) != "NULL"):
        if((json1_dict.get('Other_Key_Ingredient_1')) == ((json2_dict.get('Other_Key_Ingredient_1')) or 
        (json2_dict.get('Other_Key_Ingredient_2')) or 
        (json2_dict.get('Other_Key_Ingredient_3')))):
            other_key_ingredient_1_score = OTHER_KEY_INGREDIENT_SCORE

    print(f"other_key_ingredient_1_score ==> {other_key_ingredient_1_score}")

    other_key_ingredient_2_score =0
    if((json1_dict.get('Other_Key_Ingredient_2')) != "NULL"):
        if((json1_dict.get('Other_Key_Ingredient_2')) == ((json2_dict.get('Other_Key_Ingredient_1')) or 
        (json2_dict.get('Other_Key_Ingredient_2')) or 
        (json2_dict.get('Other_Key_Ingredient_3')))):
            other_key_ingredient_2_score = OTHER_KEY_INGREDIENT_SCORE

    print(f"other_key_ingredient_2_score ==> {other_key_ingredient_2_score}")

    other_key_ingredient_3_score =0
    if((json1_dict.get('Other_Key_Ingredient_3')) != "NULL"):
        if((json1_dict.get('Other_Key_Ingredient_3')) == ((json2_dict.get('Other_Key_Ingredient_1')) or 
        (json2_dict.get('Other_Key_Ingredient_2')) or 
        (json2_dict.get('Other_Key_Ingredient_3')))):
            other_key_ingredient_3_score = OTHER_KEY_INGREDIENT_SCORE

    print(f"other_key_ingredient_3_score ==> {other_key_ingredient_3_score}")

    total_score = 0
    total_score = (primary_protein_match_score + secondary_protein_match_score + tertiary_protein_match_score 
    + cheese_type_match_score + letuce_type_match_score 
    + other_key_ingredient_1_score + other_key_ingredient_2_score + other_key_ingredient_3_score)

    print(f"total_score protein + cheeseType + Letucetype + Other Key Ingrdeint Score ==> {total_score}")

    Key_Ingredient_Score = round(total_score/total_possible_menu_item_score*Total_category_value, 2)

    print(f"weighted Key_Ingredient_Score ==> {Key_Ingredient_Score}")

    for x in match_table:
        if(match_table[x].get('percentage_match') == mround):
            ingredient_match_weight = match_table[x].get('ingredient_match')
            print(f"Final Ingredient_match_weight ==> {ingredient_match_weight}")

    Menu_Item_Ingredient_Value = (ingredient_match_weight)*(Key_Ingredient_Score)

    print(f"Final Menu_Item_Ingredient_Value ==> {Menu_Item_Ingredient_Value}")


    #key_Feature calculations

    key_feature_1_score =0
    if((json1_dict.get('Key_Feature_1')) != "NULL"):
        if((json1_dict.get('Key_Feature_1')) == ((json2_dict.get('Key_Feature_1')) or 
        (json2_dict.get('Key_Feature_2')) or 
        (json2_dict.get('Key_Feature_3')))):
            key_feature_1_score = 33.33

    print(f"key_feature_1_score ==> {key_feature_1_score}")

    key_feature_2_score =0
    if((json1_dict.get('Key_Feature_2')) != "NULL"):
        if((json1_dict.get('Key_Feature_2')) == ((json2_dict.get('Key_Feature_1')) or 
        (json2_dict.get('Key_Feature_2')) or 
        (json2_dict.get('Key_Feature_3')))):
            key_feature_2_score = 33.33

    print(f"key_feature_2_score ==> {key_feature_2_score}")

    key_feature_3_score =0
    if((json1_dict.get('Key_Feature_3')) != "NULL"):
        if((json1_dict.get('Key_Feature_3')) == ((json2_dict.get('Key_Feature_1')) or 
        (json2_dict.get('Key_Feature_2')) or 
        (json2_dict.get('Key_Feature_3')))):
            key_feature_3_score = 33.33

    print(f"key_feature_1_score ==> {key_feature_1_score}")

    key_feature_score = 0
    key_feature_score = ((key_feature_1_score + key_feature_2_score + key_feature_3_score)/TOTAL_POSSIBLE_KEY_FEATURE)

    print(f"key_feature_score ==> {key_feature_score}")

    for x in match_table:
        if(match_table[x].get('percentage_match') == mround):
            name_match_weight = match_table[x].get('feature_match')
            print(name_match_weight)

    Key_Feature_Value = (name_match_weight)*(key_feature_score)

    print(f"Final Key_Feature_Value ==> {Key_Feature_Value}")

    Total_Comparitive_Score = round((Category_value + Menu_Item_Name_Value + Menu_Item_Ingredient_Value + Key_Feature_Value), 2)

    print(f"Total_Comparitive_Score = {Total_Comparitive_Score}")
    return(Total_Comparitive_Score)