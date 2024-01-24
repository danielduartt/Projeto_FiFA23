import streamlit as st 
import pandas as pd 



df_data = pd.read_csv("CLEAN_FIFA23_official_data.csv", index_col = 0)


st.markdown("# FIFA23 OFFICIAL DATAST! ⚽")
st.markdown("---")
clubes = df_data["Club"].value_counts().index

club = st.sidebar.selectbox("Clubes", clubes)

df_players = df_data[df_data["Club"] == club]
players = df_data["Name"].value_counts().index

player_escolhido = st.sidebar.selectbox("Jogadores", players)

player_stats = df_data[df_data["Name"] == player_escolhido].iloc[0]
st.image(player_stats["Photo"] )

st.title(f"{player_stats['Name']}")
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")


col1, col2, col3 = st.columns(3)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)']/100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f} kg")

st.divider()
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3 = st.columns(3)
col1.metric(label = "Valor de mercado", value= f"€ {player_stats['Value(£)']:.2f}")
col2.metric(label = "Remuneração Semanal", value= f"€ {player_stats['Wage(£)']:.2f}")
col3.metric(label = "Cláusula de recisão", value= f"€ {player_stats['Release Clause(£)']:.2f}")

st.markdown("---")
st.markdown("# DataFrame")
df_filtered = df_data[df_data["Club"] == club].set_index("Name")
st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")
columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", 
                                                    min_value=0, max_value=df_filtered["Wage(£)"].max()),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),
             })

st.markdow("---")
