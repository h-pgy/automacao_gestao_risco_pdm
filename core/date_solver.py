from datetime import datetime


class DataHoje:

    meses = {
        1 : 'jan',
        2 : 'fev',
        3 : 'mar',
        4 : 'abr', 
        5 : 'mai',
        6 : 'jun',
        7 : 'jul',
        8 : 'ago',
        9 : 'set',
        10 : 'out',
        11 : 'nov',
        12 : 'dez'
        }

    def __init__(self):

        self.hoje = datetime.today()

    @property
    def mes(self):

        return self.hoje.month

    @property
    def ano(self):

        return self.hoje.year

    @property
    def mes_atual_str(self):

        return self.meses[self.mes]

    @property
    def mes_seguinte_str(self):

        return self.meses[self.mes+1]

    