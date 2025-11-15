"""
Funções auxiliares para o projeto de otimização de energia
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sqlite3

def gerar_dados_consumidores(n=100):
    """Gera dados simulados de consumidores"""
    np.random.seed(42)
    
    tipos = ['Residencial', 'Comercial', 'Industrial']
    regioes = ['Norte', 'Sul', 'Leste', 'Oeste', 'Centro']
    
    consumidores = pd.DataFrame({
        'id_consumidor': range(1, n + 1),
        'nome': [f'Consumidor_{i}' for i in range(1, n + 1)],
        'tipo_consumidor': np.random.choice(tipos, n, p=[0.6, 0.3, 0.1]),
        'regiao': np.random.choice(regioes, n),
        'data_cadastro': pd.date_range(start='2023-01-01', periods=n, freq='3D')
    })
    
    return consumidores

def gerar_dados_tarifas():
    """Gera dados de tarifas por horário"""
    tarifas = pd.DataFrame({
        'id_tarifa': [1, 2, 3],
        'nome_tarifa': ['Tarifa Pico', 'Tarifa Fora Pico', 'Tarifa Intermediária'],
        'tipo_horario': ['Pico', 'Fora_Pico', 'Intermediario'],
        'valor_kwh': [0.85, 0.45, 0.65],
        'vigencia_inicio': ['2024-01-01'] * 3,
        'vigencia_fim': ['2024-12-31'] * 3
    })
    
    return tarifas

def classificar_horario(hora):
    """Classifica horário em Pico, Fora Pico ou Intermediário"""
    if 18 <= hora <= 21:  # Horário de pico: 18h às 21h
        return 1  # Pico
    elif 0 <= hora <= 6:  # Madrugada
        return 2  # Fora de Pico
    else:
        return 3  # Intermediário

def gerar_dados_consumo(consumidores_df, dias=30):
    """Gera dados simulados de consumo por hora"""
    np.random.seed(42)
    
    registros = []
    id_consumo = 1
    
    data_inicio = datetime(2024, 10, 1)
    
    for _, consumidor in consumidores_df.iterrows():
        # Consumo base por tipo
        if consumidor['tipo_consumidor'] == 'Residencial':
            consumo_base = np.random.uniform(5, 15)
        elif consumidor['tipo_consumidor'] == 'Comercial':
            consumo_base = np.random.uniform(20, 50)
        else:  # Industrial
            consumo_base = np.random.uniform(100, 300)
        
        for dia in range(dias):
            for hora in range(24):
                data_hora = data_inicio + timedelta(days=dia, hours=hora)
                
                # Variação por horário
                if 18 <= hora <= 21:  # Pico
                    fator = np.random.uniform(1.5, 2.0)
                elif 0 <= hora <= 6:  # Madrugada
                    fator = np.random.uniform(0.3, 0.6)
                else:
                    fator = np.random.uniform(0.8, 1.2)
                
                consumo_kwh = consumo_base * fator
                id_tarifa = classificar_horario(hora)
                
                # Calcular custo (será atualizado no ETL)
                valor_kwh = [0.85, 0.45, 0.65][id_tarifa - 1]
                custo_total = consumo_kwh * valor_kwh
                
                registros.append({
                    'id_consumo': id_consumo,
                    'id_consumidor': consumidor['id_consumidor'],
                    'data_hora': data_hora,
                    'consumo_kwh': round(consumo_kwh, 2),
                    'id_tarifa': id_tarifa,
                    'custo_total': round(custo_total, 2)
                })
                
                id_consumo += 1
    
    return pd.DataFrame(registros)

def gerar_dados_picos(dias=30):
    """Gera dados de picos de demanda"""
    np.random.seed(42)
    
    data_inicio = datetime(2024, 10, 1)
    registros = []
    
    for dia in range(dias):
        for hora in range(24):
            data_hora = data_inicio + timedelta(days=dia, hours=hora)
            
            # Demanda varia com horário e temperatura
            if 18 <= hora <= 21:
                demanda_base = np.random.uniform(800, 1200)
            elif 0 <= hora <= 6:
                demanda_base = np.random.uniform(300, 500)
            else:
                demanda_base = np.random.uniform(500, 800)
            
            temperatura = np.random.uniform(20, 35)
            
            registros.append({
                'id_pico': len(registros) + 1,
                'data_hora': data_hora,
                'demanda_total_mw': round(demanda_base, 2),
                'temperatura_celsius': round(temperatura, 2),
                'dia_semana': data_hora.strftime('%A')
            })
    
    return pd.DataFrame(registros)

def calcular_economia_potencial(df_consumo, df_tarifas):
    """Calcula economia potencial com otimização de horários"""
    # Merge com tarifas
    df = df_consumo.merge(df_tarifas, on='id_tarifa')
    
    # Custo atual
    custo_atual = df['custo_total'].sum()
    
    # Simular custo se todo consumo fosse em horário fora de pico
    tarifa_fora_pico = df_tarifas[df_tarifas['tipo_horario'] == 'Fora_Pico']['valor_kwh'].values[0]
    custo_otimizado = df['consumo_kwh'].sum() * tarifa_fora_pico
    
    economia = custo_atual - custo_otimizado
    percentual = (economia / custo_atual) * 100
    
    return {
        'custo_atual': custo_atual,
        'custo_otimizado': custo_otimizado,
        'economia_potencial': economia,
        'percentual_economia': percentual
    }
