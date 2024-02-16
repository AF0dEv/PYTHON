import pandas as pd 
data = [('Pedro', 18, 7),
        ('Ricardo', 15, 6),
        ('Joana', 17, 8),
        ('Miguel', 18, 7),
        ('Rita', 17, 5) ]
data_df = pd.DataFrame(data)
novo_df = df.rename(columns={0: 'Nome', 1: 'Idade', 2:'Pontuação'})
print(novo_df)