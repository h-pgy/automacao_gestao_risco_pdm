from pydoc import Doc
import pandas as pd
from docx import Document
from docx.document import Document as doc_type
from .utils import list_files


class WordReader:
    '''Reads the word file and returns it as python object'''

    orginal_data_dir = 'original_data'
    
    def check_word_files(self, words):
        '''Asserts only one word file on directory'''

        if len(words) < 1:
            raise RuntimeError('Nenhum documento de word encontrado! - extensao deve ser docx')

        elif len(words) > 1:
            raise RuntimeError('Mais de um documento de word encontrado! Manter apenas o que se deseja atualizar')

    def get_word_file(self, dir_ = None):
        '''Returns full path of word file'''

        if dir_ is None:
            dir_ = self.orginal_data_dir

        words = list_files(dir_, 'docx')

        self.check_word_files(words)

        return words[0]

    def open_doc(self, word_path=None):
        '''Opens word file'''

        if word_path is None:
            word_path = self.get_word_file()

        return Document(word_path)

    def __call__(self):

        return self.open_doc()

class TableParser:
    '''Parsed docx tables'''

    def __init__(self, doc=None):

        if doc is None:
            read_doc = WordReader()
            doc = read_doc()
        
        if not (type(doc) is doc_type):
            raise ValueError("Doc must be a pydocx document!")

        self.doc = doc

    def get_tables(self, doc=None):
        '''Lists document tables'''

        if doc is None:
            doc = self.doc
        
        #make sure it's not a generator
        return list(doc.tables)


    def parse_line(self, row):
        '''Parses table lines'''
    
        return [{'text' : cell.text, 'val' : cell} for cell in row.cells]

    
    def parse_table(self, table):
        '''Parses document table, returns a list of dicts, each dict represneting the value 
        and the correspondign cell in the word doc as the data, and col_names as a list of strings'''
        
        data = []
        for i, row in enumerate(table.rows):
           
            line = self.parse_line(row)
            data.append(line)
        return data

    def __call__(self):

        tables = self.get_tables()

        for table in tables:
            yield self.parse_table(table)


def table_generator(doc=None):

    t = TableParser(doc)

    return t()

    

    
    
