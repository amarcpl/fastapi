import json
import re

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from objdict import ObjDict

from app.hmstokenize import *
from app.map import *
from app.compare import *

from fastapi.responses import Response
from fastapi.requests import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

class Menu(BaseModel):
    menu_category: str
    menu_item_name: str
    menu_description: str

class Standard(BaseModel):
    category: str
    item_Name_1: str
    item_Name_2: str
    item_Name_3: str
    item_Name_4: str
    primary_protein: str
    secondary_protein: str
    tertiary_protein: str
    cheese_Type: str
    lettuce_Type: str
    other_Key_Ingredient_1: str
    other_Key_Ingredient_2: str
    other_Key_Ingredient_3: str
    key_Feature_1: str
    key_Feature_2: str
    key_Feature_3: str

app = FastAPI()


@app.post("/compare/")
def compare_models(json_data1 , json_data2):

    print(type(json_data1))

    host_menu_dict = json.loads(json_data1)
    comp_menu_dict = json.loads(json_data2)

    print(type(host_menu_dict))

    # host_menu = json.loads(host_menu_dict)
    # comp_menu = json.loads(comp_menu_dict)
    # print(type(host_menu))
    # score = compare_menus_and_score(host_menu, comp_menu)

    score = compare_menus_and_score(host_menu_dict, comp_menu_dict)
    return(score)
    #print(score)


@app.post("/attirb/")
#@app.post("/attirb/", response_model=Standard)
def create_attrib_structure(menu: Menu):
    words = extract_tokens_from_text(menu.menu_item_name, menu.menu_description)
    #print(words)
    collate = hms_custom_tweak(words)
    #print(collate)
    items = generate_menu_structure(menu.menu_category, menu.menu_item_name, collate)
    #print(items)
    return items
    #return JSONResponse(content=items)
    #return Response(content=items)


@app.get("/tokens/")
def get_tokens(menu_item_name : str, menu_description : str):
    words=[]
    words = extract_tokens_from_text(menu_item_name, menu_description)
    return words

