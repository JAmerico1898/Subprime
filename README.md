# Crise Subprime: Cronologia e Impactos Globais

![Aplicativo Streamlit sobre a Crise Subprime](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

Um aplicativo Streamlit interativo que oferece uma análise aprofundada da Crise Subprime de 2008, suas causas, cronologia, impactos globais e lições aprendidas. Este recurso educacional foi projetado para auxiliar professores de finanças em suas aulas sobre crises bancárias e financeiras.

## 📊 Demonstração

![image](https://github.com/user-attachments/assets/5c5cfdb3-3f83-4991-8b70-eb9b91b2bf96)

## 🚀 Características

O aplicativo oferece uma experiência educacional completa, dividida em 7 seções interativas:

- **Introdução**: Visão geral da crise e seus principais impactos
- **Linha do Tempo**: Cronologia detalhada dos eventos desde 2001 até o legado pós-crise
- **Bolha Imobiliária**: Análise da formação e colapso da bolha imobiliária nos EUA
- **Impacto Global**: Visualizações interativas sobre crescimento econômico, desemprego e dívida pública
- **Securitização**: Diagrama explicativo dos instrumentos financeiros complexos no centro da crise
- **Respostas Regulatórias**: Comparação das medidas implementadas nos EUA, União Europeia e internacionalmente
- **Lições Aprendidas**: Análise das principais lições e desafios persistentes no sistema financeiro

## 🔧 Instalação e Execução

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos para Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/crise-subprime-app.git
   cd crise-subprime-app
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o aplicativo:
   ```bash
   streamlit run app.py
   ```

5. O aplicativo será aberto automaticamente em seu navegador padrão. Se não abrir, acesse:
   ```
   http://localhost:8501
   ```

## 📋 Requisitos

O arquivo `requirements.txt` contém todas as dependências necessárias:

```
streamlit==1.28.1
pandas==2.1.1
numpy==1.26.0
plotly==5.17.0
matplotlib==3.8.0
networkx==3.2.1
pillow==10.0.1
```

## 🧩 Estrutura do Projeto

```
crise-subprime-app/
├── app.py                  # Código principal do aplicativo Streamlit
├── requirements.txt        # Dependências do projeto
├── README.md               # Este arquivo
└── screenshot.png          # Screenshot do aplicativo para o README
```

## 🎓 Uso Educacional

Este aplicativo foi desenvolvido como um recurso didático para aulas sobre crises financeiras. Ele pode ser utilizado de diversas formas:

- **Em sala de aula**: Como ferramenta visual durante aulas expositivas
- **Estudo individual**: Para alunos explorarem os conceitos em seu próprio ritmo
- **Trabalhos em grupo**: Para facilitar discussões sobre diferentes aspectos da crise
- **Material complementar**: Como recurso adicional ao material didático tradicional

## 🔍 Personalização

O aplicativo pode ser facilmente adaptado às suas necessidades:

1. Modifique o conteúdo no arquivo `app.py` para alterar textos, adicionar ou remover seções
2. Ajuste as visualizações para enfatizar aspectos específicos da crise
3. Personalize o estilo visual através das configurações CSS no início do código

## 📝 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE) - veja o arquivo LICENSE para detalhes.

## ✨ Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fork este repositório
2. Criar um branch para suas modificações (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para o branch (`git push origin feature/nova-feature`)
5. Abrir um Pull Request

## 👏 Agradecimentos

- Desenvolvido originalmente como material didático para aulas de finanças
- Inspirado por diversas análises acadêmicas sobre a Crise Subprime
- Baseado em dados de fontes como FMI, Banco Mundial e Federal Reserve
