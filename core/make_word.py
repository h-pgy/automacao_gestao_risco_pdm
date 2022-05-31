from .excel_reader import ExcelReader
from .word_reader import WordReader, table_generator
from .date_solver import DataHoje
from .utils import solve_dir


class WordMaker:

    def __init__(self):

        self.read_word = WordMaker()
        self.doc = self.read_word()
        self.word_tables = table_generator(self.doc)

        self.excel = ExcelReader()
        self.hoje = DataHoje()

    def num_meta(self, word_table):
    
        primeira_linha = word_table[0]
        primeira_celula = primeira_linha[0]
        
        return primeira_celula['text']
