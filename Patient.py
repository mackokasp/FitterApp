import pandas as pd


class Patient:
    df = 0
    prefernces = 0
    diseases = 0
    recommend = {'VegInCarb': -1, 'CatsClow': -1}
    supplement = []
    warnings = []

    def __init__(self):
        Patient.df = pd.read_csv('C:\Users\PC\Desktop\DIETY\Patient.csv')

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

    def calc_blood(self):  ## Analiza Parametrow krwi i moczu


        number = Patient.df['Leukocyte']
        if number < 5:
            Patient.recommend['VegInCarbMin'] = 0.7
            Patient.recommend['CatsClow'] = 1
        elif number > 5 and number < 7:
            Patient.recommend['VegInCarbMin'] = 0.2
            Patient.recommend['CatsClow'] = 0.5
        elif number > 7 and number < 8:
            Patient.warnings.append('Skontatktuj sie z lekrzem|Leukocyty')
        else:
            Patient.warnings.append('Powazne zaburzenie poziomu leukocytow')
        number = Patient.df['Erythrocyte']
        if number > 4.6 and number < 5:
            Patient.recommend['RootVegInCarbMin'] = 0.4
            Patient.recommend['ArgininaMin'] = 0
            Patient.recommend['ArgininaMax'] = 20
        elif number < 6.5 and number > 5.5:
            Patient.recommend['ArgininaMin'] = 15
            Patient.recommend['ArgininaMax'] = 50
            Patient.recommend['RootVegInCarbMin'] = 0.5
        elif number > 5 and number < 5.5:
            Patient.recommend['ArgininaMin'] = 10
            Patient.recommend['ArgininaMin'] = 30
        else:
            Patient.warnings.append(' Skonsultuj sie z lekarzem| Erytrocyty')
        number = Patient.df['Hematocrit']
        if number > 50:
            Patient.recommend['Water+'] = 1
            Patient.warnings.append('Lekarz! Hematokryt')
        number = Patient.df['Hemoglobine']
        if number > 15 and number < 16:
            Patient.warnings.append('Zwieksz trenning tlenowy')
        if number > 16 and number < 17.5:
            Patient.recommend['Water'] += 0.5
            Patient.warnings.append('Zwieksz trenning tlenowy')
        if number > 17.5:
            Patient.warnings.append('Lekarz! Hemoglobina')
        number = Patient.df['Platelets']
        if number > 15 and number < 16:
            Patient.warnings.append('Zwieksz trenning tlenowy')
        if number > 16 and number < 17.5:
            Patient.recommend['Water+'] += 0.5
            Patient.warnings.append('Zwieksz trenning tlenowy')
        if number > 17.5:
            Patient.warnings.append('Lekarz! Hemoglobina')
        number = Patient.df['Ob']
        if number < 5 and number > 2:
            Patient.recommend['ImbirInLipidsMin'] = 0.3
            Patient.recommend['Omega3Min'] = 1
        elif number > 5 and number < 12:
            Patient.recommend['ImbirInLipidsMin'] = 0.5
            Patient.recommend['Omega3Min'] = 1.6
            Patient.warnings.append('Wizyta u ginekologa |urologa')
            Patient.recommend['Kurkumina'] = 1000
            Patient.recommend['Piperyna'] = 25
        elif number > 12:
            Patient.warnings.append('Stop Dieta! Jedz do szpitala')
        number = Patient.df['Glukoz']
        if number > 85 and number < 95:
            Patient.recommend['Fernerator'] = 200 + (number - 85) * 20
            Patient.recommend['Berberyna'] = 200 + (number - 85) * 20
            Patient.recommend['Kakao'] = 2.5
        elif number > 95 and number < 105:
            Patient.recommend['Fernerator'] = 600
            Patient.recommend['Berberyna'] = 600 + (number - 95) * 20
            Patient.recommend['Kakao'] = 5
            Patient.warnings.append('Przejdz na HighCarb')
        elif number > 105:
            Patient.warnings.append('Cukrzyca!glukoaza')
        number = Patient.df['Insulin']
        if number > 5 and number < 7:
            Patient.recommend['ImbirInLipidsMin'] = 0.4
            Patient.recommend['OneAcidInLipids'] = 0.3
        elif number > 7:
            Patient.warnings.append('Cukrzyca! insulina')
