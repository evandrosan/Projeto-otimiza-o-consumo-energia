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

