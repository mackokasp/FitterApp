import Calculator
class Meal:
    macros = 0
    ingredients=[]
    name =0
    def adjust(self,targets):
        calc= Calculator.Calculator()
        if Meal.Kcal < targets['Proteins'] * 0.85 or Meal.Kcal > targets['Protiens'] * 1.1:
            prot=Meal.find_protein()
            Meal.modify_ingredient(prot,(targets['Protiens']/calc.get_ingredient(Meal.ingredients[prot])['Proteins'])-1)
        if Meal.Kcal < targets['Lipids'] * 0.85 or Meal.Kcal > targets['Lipids'] * 1.1:
            prot=Meal.find_protein()
            Meal.modify_ingredient(prot,(targets['Lipids']/calc.get_ingredient(Meal.ingredients[prot])['Lipids'])-1)
        if Meal.Kcal < targets['Carbs'] * 0.85 or Meal.Kcal > targets['Carbs'] * 1.1:
            prot=Meal.find_protein()
            Meal.modify_ingredient(prot,(targets['Carbs']/calc.get_ingredient(Meal.ingredients[prot])['Carbs'])-1)


    def __init__ (self,name,ingredients,macros):
        Meal.ingredients=ingredients
        Meal.macros=macros
        Meal.name = name 












    def multiply (self , number):
        Meal.kcal *= number
        Meal.proteins *= number
        Meal.lipids *= number
        Meal.carbs *= number
        Meal.amounts *= number
        return


        return

    def find_protein (self):
        bestScore = 0
        i=0
        f=-1
        calc = Calculator.Calculator()
        for ingredient in  Meal.ingredients:
            score = calc.get_ingredient(ingredient)['Proteins'] * Meal.amounts[i]
            if score > bestScore:
                bestScore = score
                f=i
            i=i+1
        return f


    def find_lipid (self):
        bestScore = 0
        i=0
        f=-1
        calc = Calculator.Calculator()
        for ingredient in  Meal.ingredients:
            score = calc.get_ingredient(ingredient)['Lipids'] * Meal.amounts[i]
            if score > bestScore:
                bestScore = score
                f=i
            i = i + 1
        return f

    def find_carb (self):
        bestScore = 0
        i=0
        f=-1
        calc = Calculator.Calculator()
        for ingredient in  Meal.ingredients:
            score = calc.get_ingredient(ingredient)['Carbs'] * Meal.amounts[i]
            if score > bestScore:
                bestScore = score
                f=i
            i = i + 1
        return f

    def modify_ingredient (self ,inList, multiplier):
        calc= Calculator.Calculator()

        Meal.kcal += calc.get_ingredient(Meal.ingredients[inList])['Kcal']*multiplier
        Meal.proteins += calc.get_ingredient(Meal.ingredients[inList])['Proteins']*multiplier
        Meal.lipids +=calc.get_ingredient(Meal.ingredients[inList])['Lipds']*multiplier
        Meal.carbs += calc.get_ingredient(Meal.ingredients[inList])['Proteins']*multiplier
        Meal.amounts[inList] *= (multiplier+1)