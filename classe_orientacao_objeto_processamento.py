#classe de Dados da dos utilizada no arquivo 3_funcoes_orientacao_objeto_mesclagem_dados.py
import json
import csv

class Dados:

    #construtor
    ##
    #def __init__(self, path, tipo_dados):
    #    self.__path = path
    #    self.__tipo_dados = tipo_dados
    #    self.dados = self.leitura_dados()
    #    self.nome_colunas = self.__get_columns()
    #    self.qtd_linhas = self.__size_data()
    
    def __init__(self, dados):
        self.dados = dados
        self.nome_colunas = self.__get_columns()
        self.qtd_linhas = self.__size_data()

       
   
    #métodos
    #método privado
    def __leitura_json(path):
        dados_json = []
        with open(path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    #método privado
    def __leitura_csv(path):
        dados_csv = []
        with open(path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    #método público
    #def leitura_dados(self):
    #    dados = []
    #    if self.__tipo_dados == 'csv':
    #        dados = self.__leitura_csv()
    #    elif self.__tipo_dados == 'json':
    #        dados = self.__leitura_json()
    #    elif self.__tipo_dados == 'list':
    #        dados = self.__path
    #        self.__path = 'lista em memória'
    #    return dados
    
    #método privado
    #permite que receba a classe como parâmetro e não o objeto
    #vai instaciar a classe
    @classmethod
    def leitura_dados(cls, path, tipo_dados):
        dados = []

        if tipo_dados == 'csv':
            dados = cls.__leitura_csv(path)
        
        elif tipo_dados == 'json':
            dados = cls.__leitura_json(path)

        return cls(dados)

    #método privado
    def __get_columns(self):
        return list(self.dados[-1].keys())
    
    #método público
    def rename_columns(self, key_mapping):
        new_dados = []
        
        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)
                
        self.dados = new_dados
        self.nome_colunas = self.__get_columns()

    #método privado
    def __size_data(self):
        return len(self.dados)

    #método estático
    def join(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)

        #return Dados(combined_list, 'list')
        return Dados(combined_list)

    #método privado
    def __transformando_dados_tabela(self):
        
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponivel'))
            dados_combinados_tabela.append(linha)
        
        return dados_combinados_tabela

    #método público
    def salvando_dados(self, path):

        dados_combinados_tabela = self.__transformando_dados_tabela()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)