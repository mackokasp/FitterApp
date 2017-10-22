import math as mt


class Meal:
    macros = 0
    ingredients=[]
    name =0

    def __init__ (self,name,ingredients,macros):
        self.ingredients=ingredients
        self.macros=macros
        self.name = name

    def adjust (self,targets):
        if self.macros['Proteins'] > 1.3 * targets['Proteins'] or self.macros['Proteins'] < 0.75 * targets['Proteins']:
            multi =  mt.sqrt(targets['Proteins'] / self.macros['Proteins'])
            self.modify_ingredient(self.find_param('Proteins'),multi)
        if self.macros['Lipids'] > 1.3 * targets['Lipids'] or self.macros['Lipids'] < 0.75 * targets['Lipids']:
            multi =  mt.sqrt(targets['Lipids'] /  self.macros['Lipids'])
            self.modify_ingredient(self.find_param('Lipids'),multi)
        if self.macros['Carbs'] > 1.3 * targets['Carbs'] or self.macros['Carbs'] < 0.75 * targets['Carbs']:
            multi =  mt.sqrt(targets['Carbs'] /  self.macros['Carbs'])
            self.modify_ingredient(self.find_param('Carbs'),multi)
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
        print
        for i in range(0,self.ingredients.shape[0]):

            score = self.ingredients[param].iloc[i]
            if score > bestScore:
                bestScore = score
                f=i

        return f

    def present(self):
        print self.name
        print self.macros
        print self.ingredients



    def modify_ingredient (self ,inList, multi):

        multiplier = multi -1
        self.macros['Kcal'] += self.ingredients['Kcal'].iloc[inList]*multiplier
        self.ingredients['Kcal'].iloc[inList] += self.ingredients['Kcal'].iloc[inList] * multiplier
        self.macros['Proteins'] += self.ingredients['Proteins'].iloc[inList] * multiplier
        self.ingredients['Proteins'].iloc[inList] += self.ingredients['Proteins'].iloc[inList] * multiplier
        self.macros['Carbs'] += self.ingredients['Carbs'].iloc[inList] * multiplier
        self.ingredients['Carbs'].iloc[inList] += self.ingredients['Carbs'].iloc[inList] * multiplier
        self.macros['Lipids'] += self.ingredients['Lipids'].iloc[inList] * multiplier
        self.ingredients['Lipids'].iloc[inList] += self.ingredients['Lipids'].iloc[inList] * multiplier
        self.ingredients['Amount'].iloc[inList] = self.ingredients['Amount'].iloc[inList] * multi
        return

