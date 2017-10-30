import psycopg2
import psycopg2.extras
import numpy as np
import pandas.io.sql as pdsql
import Meal
class Calculator:
    conn = 0

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                " dbname='dbfiiter' user='dbfitter' host='localhost' password='dbfitter' port='5432'")
        except:
            print 'Nie udalo sie polaczyc'

    def calc_meal(self, mealid):
        result = {'Kcal': 0, 'Proteins': 0, 'Lipids': 0, 'Carbs': 0}
        curs = self.conn.cursor()
        query = 'select sum(a.kcal* a.amount) as kcal, sum (a.proteins*a.amount)  as proteins, sum (a.lipids*a.amount) as lipids, sum (a.carbs*a.amount) as carbs from     (select i.kcal as kcal , mi.amount as amount, mi.mealid as mealid, i.proteins as proteins , i.lipids as lipids ,i.carbs as carbs from ingredient as i inner join mealingredient as mi on mi.ingredientid = i.id) a  where a.mealid=' + str(
            mealid)
        curs.execute(query)
        row = curs.fetchall()
        for macro in row:
            result['Kcal'] = macro[0]
            result['Proteins'] = macro[1]
            result['Lipids'] = macro[2]
            result['Carbs'] = macro[3]
        curs.close()
        return result

    def find_meal(self,dayTime,dietPlan,dietetic):
        x = []
        curs = self.conn.cursor()
        query='Select id from meal where is'+dayTime+'>0 and is'+dietPlan+'>0'
        if dietetic > 0:
            query = query +'and isdietetic>1'

        curs.execute(query)
        rows=curs.fetchall()
        for meal in rows:
            x.append(meal[0])
        curs.close()
        return x

    def select_meal(self,list,targetMacros):                           ## trzeba to jakos poprawic
        bestMeal = 0
        bestScore =999999
        for meal in list:
            mealMacros =self.calc_meal(meal)
            score = (mealMacros['Proteins'] - targetMacros['Proteins'])**2
            score = score + (mealMacros['Lipids'] - targetMacros['Lipids'])**2
            score = score + ((mealMacros['Carbs'] - targetMacros['Carbs']))**2

            if score < bestScore:
                bestMeal = meal
                bestScore =score
        M=self.create_meal(bestMeal)
        return M




    def get_ingredient (self,id):
        result = {'Kcal': 0, 'Proteins': 0, 'Lipids': 0, 'Carbs': 0}
        curs= self.conn.cursor()
        query = 'Select kcal, proteins,lipids,carbs  from ingredient where id ='+str(id)
        curs.execute(query)
        row = curs.fetchall()
        for macro in row:
            result['Kcal'] = macro[0]
            result['Proteins'] = macro[1]
            result['Lipids'] = macro[2]
            result['Carbs'] = macro[3]
            curs.close ()
            return result


    def get_meal_ingredients (self,mealid):
        df=0
        query = 'select * from (select mi.mealid as Mealid,i.name as name , i.id as ingredientid  , mi.amount as Amount,i.kcal as Kcal  , i.proteins as Proteins , i.lipids as Lipids ,i.carbs as Carbs from ingredient as i inner join mealingredient as mi on mi.ingredientid = i.id) a where a.mealid ='   + str(mealid)
        df = pdsql.read_sql_query(query, self.conn)
        df.columns = ['Mealid' , 'Name' ,'Id' , 'Amount', 'Kcal', 'Proteins', 'Lipids', 'Carbs']
        df['Kcal'] =  df['Kcal']*df['Amount']
        df['Carbs'] = df['Carbs'] * df['Amount']
        df['Proteins'] = df['Proteins'] * df['Amount']
        df['Lipids'] = df['Lipids'] * df['Amount']
        return df

    def get_name (self , mealid):
        query = 'Select  name  from meal where id =' + str(mealid)
        curs= self.conn.cursor()
        curs.execute(query)
        row = curs.fetchall()
        for i in row:
            name = i[0]
            curs.close()
            return name





    def create_meal (self , mealid):
        mealigredients =  self.get_meal_ingredients(mealid)

        macros = self.calc_meal(mealid)

        name = self.get_name(mealid)

        meal = Meal.Meal(name,mealigredients,macros )
        return meal



    def get_diet (self ,name):
        query = 'Select  proteins , lipids , carbs,kcal  from dietinfo where name =\'' + name + '\''

        result = {'Kcal': 0, 'Proteins': 0, 'Lipids': 0, 'Carbs': 0}
        curs = self.conn.cursor()
        curs.execute(query)
        row = curs.fetchall()
        for macro in row:
            result['Proteins'] = macro[0]
            result['Lipids'] = macro[1]
            result['Carbs'] = macro[2]
            result['Kcal'] = macro[3]
            return result

















