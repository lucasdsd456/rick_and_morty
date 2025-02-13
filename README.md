# README - Rick and Morty Characters Viewer

Este projeto é um site criado com Streamlit que exibe personagens da série *Rick and Morty* com suas principais informações e número de aparições por temporada.

## 🛠️ Requisitos
- Python 3.x
- Streamlit

## 📂 Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/lucasdsd456/rick_and_morty.git
   cd rick_and_morty
   ```
2. Instale as dependências:
   ```bash
   pip install streamlit
   ```

## 🚀 Como Executar
1. Certifique-se de ter o arquivo `characters.json` na pasta do projeto.
2. Execute o comando:
   ```bash
   streamlit run app.py
   ```
3. Acesse o navegador no endereço indicado.

## 📝 Descrição do Código
- O arquivo `app.py` lê os dados de `characters.json`.
- Calcula aparições por temporada.
- Exibe cada personagem em um card com:
  - Imagem, Nome, Status, Espécie, Gênero, Origem, Localização e Aparições.

## 📌 Estrutura do Projeto
```
📂 RICK_AND_MORTY
│── app.py
└── characters.json
└── .gitattributes
```

## 💡 Exemplo de Uso
- Ao acessar a aplicação, serão exibidos cards com as informações de cada personagem.

---
Contribua e personalize! 🚀