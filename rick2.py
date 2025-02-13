import json
import streamlit as st

file_path = 'characters.json'
with open(file_path, 'r') as file:
    data = json.load(file)

temporadas = {
    'Temporada 1': range(1, 12),
    'Temporada 2': range(12, 22),
    'Temporada 3': range(22, 32)
}

st.title('Rick and Morty Characters')

for character in data:
    aparicoes = {season: sum(1 for ep in character['episode'] if int(ep.split('/')[-1]) in eps) for season, eps in temporadas.items()}
    
    with st.container():
        st.image(character['image'], width=150)
        st.subheader(character['name'])
        st.write(f"**ID:** {character['id']}")
        st.write(f"**Status:** {character['status']}")
        st.write(f"**Espécie:** {character['species']}")
        st.write(f"**Gênero:** {character['gender']}")
        st.write(f"**Origem:** {character['origin']['name']}")
        st.write(f"**Localização:** {character['location']['name']}")
        st.write(f"**Aparições Totais:** {len(character['episode'])}")
        for season, count in aparicoes.items():
            st.write(f"{season}: {count} aparições")
        st.write(f"**Criado em:** {character['created']}")
        st.markdown("---")
