import csv
from questions import question
filePath = "survey.csv"

#survey class
class survey:
    def __init__(self):
        self.questions = []
        self.regions = ['Abruzzo', 'Basilicata', 'Calabria', 'Campania', 'Emilia-Romagna', 'Friuli-Venezia Giulia', 'Lazio', 'Liguria', 'Lombardy', 'Marches', 'Molise', 'Piedmont', 'Apulia', 'Sardinia', 'Sicily', 'Tuscany', 'Trentino-South Tyrol', 'Umbria', 'Aosta Valley', 'Veneto']
        #self.LoadQuesAns()
    #def Load(self):
        
    #def GiveSurvey

x = survey()
for region in x.regions:
    print(region)

q = question()
print(q.prompt)