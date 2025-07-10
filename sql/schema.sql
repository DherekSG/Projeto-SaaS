-- Criação da tabela de empresas com login via CNPJ e senha hash
CREATE TABLE empresas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cnpj VARCHAR(14) UNIQUE NOT NULL CHECK (cnpj ~ '^[0-9]{14}$'), -- Apenas números
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    senha_hash VARCHAR(255) NOT NULL, -- Armazenar senha criptografada (bcrypt recomendado)
    criada_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- Tabela de log de arquivos CSV enviados para processamento (opcional)
CREATE TABLE arquivos_upload (
    id SERIAL PRIMARY KEY,
    empresa_id INTEGER REFERENCES empresas(id),
    nome_arquivo VARCHAR(255),
    registros INTEGER,
    enviado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela principal com predições por linha de cliente/registro
CREATE TABLE predicoes_churn (
    id SERIAL PRIMARY KEY,
    empresa_id INTEGER REFERENCES empresas(id),
    data_prevista TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Dados do dataset (XGBoost com 30 variáveis normalizadas)
    cons_12m DOUBLE PRECISION,
    cons_gas_12m DOUBLE PRECISION,
    cons_last_month DOUBLE PRECISION,
    forecast_cons_12m DOUBLE PRECISION,
    forecast_cons_year DOUBLE PRECISION,
    forecast_discount_energy DOUBLE PRECISION,
    forecast_meter_rent_12m DOUBLE PRECISION,
    forecast_price_energy_off_peak DOUBLE PRECISION,
    forecast_price_energy_peak DOUBLE PRECISION,
    forecast_price_pow_off_peak DOUBLE PRECISION,
    imp_cons DOUBLE PRECISION,
    margin_gross_pow_ele DOUBLE PRECISION,
    margin_net_pow_ele DOUBLE PRECISION,
    nb_prod_act DOUBLE PRECISION,
    net_margin DOUBLE PRECISION,
    num_years_antig DOUBLE PRECISION,
    pow_max DOUBLE PRECISION,
    channel_sales_EWPAKWLLIWISIWDUIBDLFMALXOWMWPCI DOUBLE PRECISION,
    channel_sales_FIXDBUFSEFWOOAASFCXDXADSIEKOCEAA DOUBLE PRECISION,
    channel_sales_FOOSDFPFKUSACIMWKCSOSBICDXKICAUA DOUBLE PRECISION,
    channel_sales_LMKEBAMCAACLUBFXADLMUECCXOIMLEMA DOUBLE PRECISION,
    channel_sales_MISSING DOUBLE PRECISION,
    channel_sales_SDDIEDCSLFSLKCKWLFKDPOEEAILFPEDS DOUBLE PRECISION,
    channel_sales_USILXUPPASEMUBLLOPKAAFESMLIBMSDF DOUBLE PRECISION,
    has_gas_T DOUBLE PRECISION,
    origin_up_KAMKKXFXXUWBDSLKWIFMMCSIUSIUOSWS DOUBLE PRECISION,
    origin_up_LDKSSXWPMEMIDMECEBUMCIEPIFCAMKCI DOUBLE PRECISION,
    origin_up_LXIDPIDDSBXSBOSBOUDACOCKEIMPUEPW DOUBLE PRECISION,
    origin_up_MISSING DOUBLE PRECISION,
    origin_up_USAPBEPCFOLOEKILKWSDIBOSLWAXOBDP DOUBLE PRECISION,

    -- Saídas do modelo
    churn_previsto BOOLEAN,
    probabilidade_churn NUMERIC(5,4)
);
