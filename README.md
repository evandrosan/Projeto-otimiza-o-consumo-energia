# Projeto de Otimização de Consumo de Energia

##  Contexto do Desafio
O setor energético brasileiro é diversificado, abrangendo fontes como hidrelétricas, eólicas e solares. 
**Desafio**: Otimizar o consumo resulta em menor desperdício e redução de custos para consumidores.

##  Objetivo
Analisar padrões de consumo de energia e identificar oportunidades de otimização através de:
- Análise de consumo por horário (pico vs fora de pico)
- Comparação de tarifas e eficácia tarifária
- Identificação de consumidores com alto potencial de economia
- Recomendações baseadas em dados

##  Estrutura do Projeto
```
projeto_energia/
├── data/
│   ├── raw/              # Dados brutos simulados
│   └── processed/        # Dados processados
├── sql/
│   └── schema.sql        # Estrutura do banco de dados
├── notebooks/
│   ├── 01_etl_pipeline.ipynb
│   ├── 02_analise_kpis.ipynb
│   └── 03_dashboard.ipynb
├── src/
│   └── utils.py          # Funções auxiliares
└── README.md
```

##  Tecnologias
- **Python**: Pandas, NumPy, Matplotlib, Seaborn
- **SQL**: SQLite (simulação de banco de dados)
- **Jupyter Notebook**: Análise interativa

##  KPIs Principais
1. **Consumo Médio**: kWh por consumidor/período
2. **Horas de Pico**: Identificação de períodos de maior demanda
3. **Eficácia Tarifária**: Economia potencial com mudança de tarifa

##  Como Executar

### 1. Clonar o Repositório
```bash
git clone https://github.com/evandrosan/Projeto-otimiza-o-consumo-energia.git
cd Projeto-otimiza-o-consumo-energia
```

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 3. Executar os Notebooks (na ordem)
```bash
jupyter notebook
```

Abra e execute os notebooks nesta sequência:
1. **01_etl_pipeline.ipynb** - Gera os dados e cria o banco SQLite
2. **02_analise_kpis.ipynb** - Analisa os KPIs principais
3. **03_dashboard.ipynb** - Visualiza o dashboard completo

### Requisitos
- Python 3.8+
- Jupyter Notebook
- Bibliotecas: pandas, numpy, matplotlib, seaborn

### Observações
- Os dados são gerados automaticamente pelo notebook 01
- Não é necessário rodar o `utils.py` diretamente (ele é importado pelos notebooks)
- O banco de dados SQLite será criado em `data/energia.db`

##  Resultados Esperados

Após executar os notebooks, você terá:
-  Banco de dados com 72.000+ registros de consumo
-  Análises de consumo por tipo, horário e região
-  Identificação de economia potencial (até 40%)
-  Dashboard com 6 visualizações integradas
-  Recomendações estratégicas para otimização

##  Contribuições

Sinta-se à vontade para abrir issues ou pull requests!

##  Licença

Este projeto é de código aberto para fins educacionais.
