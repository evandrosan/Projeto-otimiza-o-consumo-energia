-- Schema do Banco de Dados - Sistema de Energia

-- Tabela de Consumidores
CREATE TABLE IF NOT EXISTS consumidores (
    id_consumidor INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    tipo_consumidor VARCHAR(20), -- Residencial, Comercial, Industrial
    regiao VARCHAR(50),
    data_cadastro DATE
);

-- Tabela de Tarifas
CREATE TABLE IF NOT EXISTS tarifas (
    id_tarifa INTEGER PRIMARY KEY,
    nome_tarifa VARCHAR(50),
    tipo_horario VARCHAR(20), -- Pico, Fora_Pico, Intermediario
    valor_kwh DECIMAL(10, 4),
    vigencia_inicio DATE,
    vigencia_fim DATE
);

-- Tabela de Consumo
CREATE TABLE IF NOT EXISTS consumo (
    id_consumo INTEGER PRIMARY KEY,
    id_consumidor INTEGER,
    data_hora DATETIME,
    consumo_kwh DECIMAL(10, 2),
    id_tarifa INTEGER,
    custo_total DECIMAL(10, 2),
    FOREIGN KEY (id_consumidor) REFERENCES consumidores(id_consumidor),
    FOREIGN KEY (id_tarifa) REFERENCES tarifas(id_tarifa)
);

-- Tabela de Picos de Demanda
CREATE TABLE IF NOT EXISTS picos (
    id_pico INTEGER PRIMARY KEY,
    data_hora DATETIME,
    demanda_total_mw DECIMAL(10, 2),
    temperatura_celsius DECIMAL(5, 2),
    dia_semana VARCHAR(20)
);

-- Índices para otimização de consultas
CREATE INDEX idx_consumo_consumidor ON consumo(id_consumidor);
CREATE INDEX idx_consumo_data ON consumo(data_hora);
CREATE INDEX idx_picos_data ON picos(data_hora);
