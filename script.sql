CREATE UNLOGGED TABLE clientes (
    id int PRIMARY KEY,
    limite DECIMAL(10) NOT NULL,
    saldo DECIMAL(10) NOT NULL
);

CREATE UNLOGGED TABLE transacoes (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL,
    data_transacao TIMESTAMP NOT NULL,
    tipo CHAR(1) CHECK (tipo IN ('d', 'c')),
    valor DECIMAL(10) NOT NULL,
    codigo_cliente INTEGER REFERENCES clientes(id) ON DELETE CASCADE
);

INSERT INTO clientes (id, limite, saldo) VALUES 
(1, 100000, 0),
(2, 80000, 0),
(3, 1000000, 0),
(4, 10000000, 0),
(5, 500000, 0);
