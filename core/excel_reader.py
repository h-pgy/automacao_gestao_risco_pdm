import pandas as pd
from .utils import list_files


class ExcelReader:


    orginal_data_dir = 'original_data'

    sheet_names = {
        'realizado' : 'B4_realizado_acumulado',
        'projetado' : 'B3_projetado_acumulado'
    }

    def __init__(self, file_path = None):

        if file_path is None:
            file_path = self.get_xl_file()
        
        self.file_path = file_path

        self.projetado = self.read_sheet('projetado')
        self.acumulado = self.read_sheet('realizado')

    def check_xl_files(self, files):
        '''Asserts only one word file on directory'''

        if len(files) < 1:
            raise RuntimeError('Nenhum documento de excel encontrado! - extensao deve ser xlsx')

        elif len(files) > 1:
            raise RuntimeError('Mais de um documento de excel encontrado! Manter apenas o que se deseja atualizar')

    def get_xl_file(self, dir_ = None):
        '''Returns full path of excel file'''

        if dir_ is None:
            dir_ = self.orginal_data_dir

        files = list_files(dir_, 'xlsx')

        self.check_xl_files(files)

        return files[0]

    def padronizar_colunas(self, df):

        padrao = {}

        for col_og in df.columns:
            col = str(col_og)
            col = col.lower()
            col = col.strip()
            col = col.replace(' ', '_')
            if col.startswith('met'):
                col = 'periodo'
            padrao[col_og] = col

        df = df.rename(padrao, axis=1)

        return df

            
    
    def read_sheet(self, sheet_name):

        if sheet_name not in self.sheet_names:
            raise ValueError(f'Sheet name must be in {self.sheet_names.keys()}')

        sheet_name = self.sheet_names[sheet_name]

        df = pd.read_excel(self.file_path, sheet_name=sheet_name,
                         skiprows=[0,1], header=0)

        df = self.padronizar_colunas(df)
        
        return df