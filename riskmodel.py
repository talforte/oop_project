from securitylist import SecurityList
from dbmodel import dbmodel



class riskModel(): # מודל לחישוב רמת סיכון
    def __init__(self):
        self.db = dbmodel()
        self.sl = SecurityList()


    def calculate_risk(self, sector, changes, type): # מחשב סיכון של מנייה \ אג"ח אחת
        sector_weights = {
            'technology': 6,
            'flight':5,
            'transportation': 5,
            'energy': 4,
            'healthcare': 4,
            'industry': 3,
            'finance': 3,
            'real estate': 2,
            'industry': 1
        }
        
        change_weights = {
            'low changes': 1,
            'big changes': 2
        }
        
        type_weights = {
            'regular stock': 1,
            'preferred stock': 1,
            'government bond': 0.5,
            'corporate bond': 0.1
        }
        
        A = sector_weights.get(sector, 0) * 0.5
        B = change_weights.get(changes, 0) * 0.3
        Y = type_weights.get(type, 0) * 0.2
        
        risk = A + B + Y
        return risk
    
    
    def calc_average_risk(self): #מחשב את הסיכון הממוצע של כל ההשקעות
        total_risk = 0
        for key in self.db:
            total_risk += self.calculate_risk(self.db[key]['sector'], self.db[key]['changes'], self.db[key]['type'])
        average_risk = total_risk / len(self.db)
        return average_risk
