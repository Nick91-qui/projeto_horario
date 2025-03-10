import pandas as pd

# Carregar o arquivo CSV original
arquivo = "horario_escolar.csv"
df = pd.read_csv(arquivo, encoding="latin1")

# Função para limpar os nomes, mantendo apenas o primeiro nome e corrigindo "Gê" para "GERLÂNDIA"
def limpar_nome(nome):
    if isinstance(nome, str):  # Verifica se é uma string
        partes = nome.split()  # Divide o nome em partes
        primeiro_nome = partes[0]  # Pega só o primeiro nome
        if primeiro_nome.lower() in ["gê", "ge", "gé"]:  # Verifica variações
            return "GERLÂNDIA"
        return primeiro_nome  # Retorna o primeiro nome normal
    return nome  # Se não for string, retorna o mesmo valor

# Aplicar a limpeza em todas as células do dataframe
df = df.applymap(limpar_nome)

# Criar uma estrutura para armazenar os horários organizados por professor
horarios = df.iloc[:, 0]  # Primeira coluna contém os horários
turmas = df.columns[1:]  # As demais colunas são turmas

# Criando um dicionário para armazenar os dados reorganizados
professores_dict = {}

# Percorrer a tabela para reorganizar os dados
for i, horario in enumerate(horarios):
    for turma in turmas:
        professor = df.loc[i, turma]  # Obtém o professor naquele horário e turma
        if pd.notna(professor):  # Evitar valores vazios
            if professor not in professores_dict:
                professores_dict[professor] = [""] * len(horarios)  # Criamos uma lista vazia do tamanho da tabela
            professores_dict[professor][i] += f"{turma}, "  # Adicionamos a turma ao horário do professor

# Criando um DataFrame com os horários e professores organizados corretamente
df_final = pd.DataFrame(professores_dict)
df_final.insert(0, "Horário", horarios)  # Inserindo a coluna de horários no início

# Removendo as vírgulas extras no final das células
df_final = df_final.map(lambda x: x.rstrip(", ") if isinstance(x, str) else x)

# Salvar o arquivo reorganizado
df_final.to_csv("saida_reorganizada.csv", index=False, encoding="utf-8-sig")

print("Arquivo reorganizado salvo como 'saida_reorganizada.csv'")
