import math as mt


class Meal:
    macros = 0
    ingredients=[]
    name =0

    def __init__ (self,name,ingredients,macros):
        Meal.ingredients=ingredients
        Meal.macros=macros
        Meal.name = name

    def adjust (self,targets):
        if Meal.macros['Proteins'] > 1.3 * targets['Proteins'] or Meal.macros['Proteins'] < 0.75 * targets['Proteins']:
            multi =  mt.sqrt(targets['Proteins'] /  Meal.macros['Proteins'])
            Meal.modify_ingredient(Meal.find_param('Proteins'),multi)
        if Meal.macros['Lipids'] > 1.3 * targets['Lipids'] or Meal.macros['Lipids'] < 0.75 * targets['Lipids']:
            multi =  mt.sqrt(targets['Lipids'] /  Meal.macros['Lipids'])
            Meal.modify_ingredient(Meal.find_param('Lipids'),multi)
        if Meal.macros['Carbs'] > 1.3 * targets['Carbs'] or Meal.macros['Carbs'] < 0.75 * targets['Carbs']:
            multi =  mt.sqrt(targets['Carbs'] /  Meal.macros['Carbs'])
            Meal.modify_ingredient(Meal.find_param('Carbs'),multi)
        return

    def resize (self , number):
        Meal.macros['Kcal'] *= number
        Meal.macros['Proteins'] *= number
        Meal.macros['Lipids'] *= number
        Meal.macros['Carbs'] *= number
        Meal.ingredients['Kcal'] *= number
        Meal.ingredients['Lipids'] *= number
        Meal.ingredients['Proteins'] *= number
        Meal.ingredients['Carbs'] *= number
        return

    def find_param (self,param):
        bestScore = 0
        i=0
        f=-1

        for ingredient in  Meal.ingredients:
            score = ingredient[param]
            if score > bestScore:
                bestScore = score
                f=i
            i=i+1
        return f

    def modify_ingredient (self ,inList, multiplier):


        Meal.macros['Kcal'] += Meal.ingredients['Kcal'].iloc[inList]*multiplier
        Meal.macros['Proteins'] += Meal.ingredients['Proteins'].iloc[inList] * multiplier
        Meal.macros['Carbs'] += Meal.ingredients['Carbs'].iloc[inList] * multiplier
        Meal.macros['Lipids'] += Meal.ingredients['Lipids'].iloc[inList] * multiplier
        return

