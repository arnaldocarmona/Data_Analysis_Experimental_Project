# Importando as bibliotecas:

'''Este código pode de inicio dar um erro, porque os valores estão separados por vírgula,
quando no pandas o padrão é ponto. Use separador ";" (ponto e vírgula) para resolver.
'''
import pandas as pd

funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=";", decimal=",")
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=";", decimal=",")

# retirar colunas de estados civil e cargo do funcionário da tabela
funcionarios_df = funcionarios_df.drop(['Estado Civil','Cargo'], axis=1)

print(funcionarios_df)
print(servicos_df)
print(clientes_df)

# 1- Cáculo de Folha Salarial

funcionarios_df['Salário Total'] = funcionarios_df['Salario Base']+funcionarios_df['Impostos']+funcionarios_df['Beneficios']+funcionarios_df['VT']+funcionarios_df['VR']
print(funcionarios_df)
print(f'O total da folha salarial mensal é de R$ {(funcionarios_df["Salário Total"].sum()):,}')


# 2 - Faturamento da Empresa
'''O ideal é pegar sempre a tabela de valores unicos e adicona-la a outra tabela que pode conter valores repetidos.
Sempre pega a tabela de características e junte ela a tabela fatos.
    Faturamentos_df = servicos_df.merge(clientes_df, on='ID Cliente') Esta é uma opção para juntar duas tabelas
pequenas sem ter que selecionar apenas as colunas.'''

faturamentos_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente', 'Valor Contrato Mensal']], on='ID Cliente')
faturamentos_df['faturamento_total'] = faturamentos_df['Tempo Total de Contrato (Meses)'] * faturamentos_df['Valor Contrato Mensal']

print(faturamentos_df)
print(f'O faturamento total é de R$ {(sum(faturamentos_df["faturamento_total"])):,}')

# 3- Percentual de Funcionários que fecharam contrato

func_fecharamcontrato = len(servicos_df['ID Funcionário'].unique())
func_total = len(funcionarios_df['ID Funcionário'])
#display(func_fecharamcontrato)
#display(func_total)
print(f'A quantidade de funcionários que fecharam contrato foi de: {(func_fecharamcontrato/func_total):.2%}')

# 4-Total de contratos por área

contratos_area_df = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']], on='ID Funcionário')

print(contratos_area_df)
contratos_area_qtde = contratos_area_df['Area'].value_counts()

print(contratos_area_qtde)
contratos_area_qtde.plot(kind='bar')

# 5-Total de funcionários por área

qtde_funcionarios_area = funcionarios_df['Area'].value_counts()

print(qtde_funcionarios_area)
qtde_funcionarios_area.plot(kind='bar')

# 6-Ticket médio mensal

ticket_médio = clientes_df['Valor Contrato Mensal'].mean()
print(f'O valor do Ticket Médio Mensal é de R$ {(ticket_médio):,.2f}')
