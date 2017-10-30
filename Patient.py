import pandas as pd


class Patient:
    df = 0
    prefernces = 0
    diseases =0
    recommend = {}
    supplement = []
    warnings = []
    targets =[]
    diet =''

    def __init__(self):
        self.df = pd.read_csv('C:\Users\PC\Desktop\DIETY\Patient.csv')
        prefernces = 0
        diseases = 0
        self.diet=self.df['Plan'].iloc[0]
        self.calc_daily()



    def present (self):
        print  self.recommend
        print self.warnings



    def calc_daily(self):
        result = {'Kcal': 0, 'Proteins': 0, 'Lipids': 0, 'Carbs': 0}  ## to jest chujowe jak barszcz
        goalRatio = 1
        if Patient.df['Goal'].iloc[0] == 'lose':
            goalRatio = 0.85
        elif Patient.df['Goal'].iloc[0] == 'gain':
            goalRatio = 1.12
        result['Kcal'] = goalRatio * 25 * Patient.df['Weight'].iloc[0] * Patient.df['Activity'].iloc[0]
        if Patient.df['Plan'].iloc[0] is None or Patient.df['Plan'].iloc[0] == 'IfItFit':  ## tutaj powinno byc wczytywanie pliku dietainfo
            result['Proteins'] = (result['Kcal'] * 0.14) / 4
            result['Lipids'] = (result['Kcal'] * 0.3) / 9
            result['Carbs'] = (result['Kcal'] * 0.56) / 4
        self.targets = result

    def calc_blood(self):  ## Analiza Parametrow krwi i moczu


        number = self.df['Leukocyte'].iloc[0]
        if number < 5:
            self.recommend['VegInCarbMin'] = 0.7
            self.recommend['CatsClow'] = 1
        elif number >= 5 and number < 7:
            self.recommend['VegInCarbMin'] = 0.2
            self.recommend['CatsClow'] = 0.5
        elif number >= 7 and number < 8:
            self.warnings.append('Skontatktuj sie z lekrzem|Leukocyty')
        else:
            self.warnings.append('Powazne zaburzenie poziomu leukocytow')
        number = self.df['Erythrocyte '].iloc[0]
        if number >= 4.6 and number < 5:
            self.recommend['RootVegInCarbMin'] = 0.4
            self.recommend['ArgininaMin'] = 0
            self.recommend['ArgininaMax'] = 20
        elif number <= 6.5 and number > 5.5:
            self.recommend['ArgininaMin'] = 15
            self.recommend['ArgininaMax'] = 50
            self.recommend['RootVegInCarbMin'] = 0.5
        elif number >= 5 and number < 5.5:
            self.recommend['ArgininaMin'] = 10
            self.recommend['ArgininaMin'] = 30
        else:
            self.warnings.append(' Skonsultuj sie z lekarzem| Erytrocyty')
        number = self.df['Hematocrit'].iloc[0]
        if number >= 50:
            self.recommend['Water+'] = 1
            self.warnings.append('Lekarz! Hematokryt')
        number = self.df['Hemoglobine'].iloc[0]
        if number >= 15 and number < 16:
            self.warnings.append('Zwieksz trenning tlenowy')
        if number >= 16 and number < 17.5:
            self.recommend['Water'] += 0.5
            self.warnings.append('Zwieksz trenning tlenowy')
        if number >= 17.5:
            self.warnings.append('Lekarz! Hemoglobina')
        number = self.df['Platelets'].iloc[0]
        if number >= 15 and number < 16:
            self.warnings.append('Zwieksz trenning tlenowy')
        if number >= 16 and number < 17.5:
            self.recommend['Water+'] += 0.5
            self.warnings.append('Zwieksz trenning tlenowy')
        if number >= 17.5:
            self.warnings.append('Lekarz! Plytki')
        number = self.df['Ob'].iloc[0]
        if number <= 5 and number > 2:
            self.recommend['ImbirInLipidsMin'] = 0.3
            self.recommend['Omega3Min'] = 1
        elif number >= 5 and number < 12:
            self.recommend['ImbirInLipidsMin'] = 0.5
            self.recommend['Omega3Min'] = 1.6
            self.warnings.append('Wizyta u ginekologa |urologa')
            self.recommend['Kurkumina'] = 1000
            self.recommend['Piperyna'] = 25
        elif number >= 12:
            self.warnings.append('Stop Dieta! Jedz do szpitala')
        number = self.df['Glukoz'].iloc[0]
        if number >= 85 and number < 95:
            self.recommend['Fernerator'] = 200 + (number - 85) * 20
            self.recommend['Berberyna'] = 200 + (number - 85) * 20
            self.recommend['Kakao'] = 2.5
        elif number >= 95 and number < 105:
            self.recommend['Fernerator'] = 600
            self.recommend['Berberyna'] = 600 + (number - 95) * 20
            self.recommend['Kakao'] = 5
            self.warnings.append('Przejdz na HighCarb')
        elif number >= 105:
            self.warnings.append('Cukrzyca!glukoaza')
        number = self.df['Insulin'].iloc[0]
        if number >= 5 and number < 7:
            self.recommend['ImbirInLipidsMin'] = 0.4
            self.recommend['OneAcidInLipids'] = 0.3
        elif number >= 7:
            self.warnings.append('Cukrzyca! insulina')
        number = self.df['Prolaktin'].iloc[0]
        if number >= 15 and number <= 30:
            self.recommend['KorzenMaca'] = 1 * self.df['Weight'].iloc[0]
            self.recommend['VitB6'] = 100
        elif number >= 30:
            self.warnings.append('Konsultacje Prolaktyna !')
        number = self.df['Testosteron'].iloc[0]
        if number <= 400 and number > 200:
            self.reccomend['Aszwaganda'] = 5
        elif number >= 400 and number < 600:
            self.reccomend['Aszwaganda'] = 3
            self.reccomend['Wapn'] = 300
            self.reccomend['D3'] = 4000

        elif number >= 600:
            self.recommend['KorzenMaca'] = 1 * self.df['Weight'].iloc[0]
            self.recommend['Wapn'] = 350

        number = self.df['Iron'].iloc[0]
        if number <= 50 and number > 31:
            self.recommend['Tatar'] = 1
            self.recommend['Kiszonki'] = 1
            self.recommend['Samme'] = 1

        elif number <= 150 and number > 120:
            self.recommend['Zelazo'] = 0.4
            self.recommend['CzerwoneMiesoNaTydzien'] = 0.4
        number = self.df['B12'].iloc[0]
        if number <= 250 and number > 180:
            self.rrecommend['B12'] = 300
        elif number <= 800 and number > 250:
            self.recommend['Iron'] = 120
            self.recommend['Eferyna'] = 200




















