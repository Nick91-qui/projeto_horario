import pandas as pd

# Carregar a planilha original (substitua pelo nome correto do arquivo)
arquivo = "horario_escolar.xlsx"
df = pd.read_excel(arquivo)

# Criar uma estrutura para armazenar os horários organizados por professor
horarios = df.iloc[:, 0]  # Primeira coluna contém os horários
turmas = df.columns[1:]  # As demais colunas são turmas

# Criando um dicionário para armazenar os dados reorganizados
professores_dict = {}

# Percorrer a tabela para reorganizar os dados
for i, horario in enumerate(horarios):
    for turma in turmas:
        professor = df.loc[i, turma]  # Obtemos o professor naquele horário e turma
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
df_final.to_excel("saida_reorganizada.xlsx", index=False)

print("Planilha reorganizada salva como 'saida_reorganizada.xlsx'")
