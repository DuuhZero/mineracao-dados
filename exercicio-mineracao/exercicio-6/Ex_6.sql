DROP TABLE IF EXISTS vendas, produtos, clientes CASCADE;

CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    idade INT
);

CREATE TABLE produtos (
    id_produto SERIAL PRIMARY KEY,
    nome_produto VARCHAR(100),
    preco NUMERIC(10,2)
);

CREATE TABLE vendas (
    id_venda SERIAL PRIMARY KEY,
    id_cliente INT,
    id_produto INT,
    quantidade INT,
    valor_total NUMERIC(10,2),
    data_venda DATE
);

-- Inserindo Clientes (30 registros)
INSERT INTO clientes (nome, email, idade) VALUES
('Ana Silva', 'ana@email.com', 28), ('Carlos Souza', 'carlos@email.com', 35),
('Beatriz Lima', 'bea@email.com', 22), ('Daniel Alves', 'daniel@email.com', 41),
('Eduardo Rocha', 'edu@email.com', 30), ('Fernanda Costa', 'fer@email.com', 27),
('Gabriel Cruz', 'gabi@email.com', 50), ('Helena Dias', 'helena@email.com', 19),
('Igor Martins', 'igor@email.com', 33), ('Julia Ramos', NULL, 24), -- [Dado Vazio]
('Lucas Mendes', 'lucas@email.com', 29), ('Mariana Barbosa', 'mari@email.com', 38),
('Natan Duarte', 'natan@email.com', -15), -- [Valor Inválido]
('Otavio Faria', 'otavio@email.com', 45), ('Patricia Melo', 'patty@email.com', 31),
('Renato Ribeiro', 'renato@email.com', 26), ('Sofia Freitas', 'sofia@email.com', 23),
('Thiago Xavier', 'thiago@email.com', 36), ('Vanessa Nunes', 'vanessa@email.com', 21),
('Wagner Moura', 'wagner@email.com', 55), ('Yara Cardoso', 'yara@email.com', 40),
('Zeca Pagodinho', 'zeca@email.com', 62), ('Alice Monteiro', 'alice@email.com', 25),
('Bruno Castro', 'bruno@email.com', 34), ('Camila Peixoto', 'camila@email.com', 29),
('Diego Teixeira', 'diego@email.com', 48), ('Elisa Guimaraes', 'elisa@email.com', 32),
('Fabio Andrade', 'fabio@email.com', 27), ('Guilherme Ramos', 'gui@email.com', 31),
('Ana Silva', 'ana@email.com', 28); -- [Duplicidade]

-- Inserindo Produtos (10 registros)
INSERT INTO produtos (nome_produto, preco) VALUES
('Teclado Mecanico', 250.00), ('Mouse Gamer', 120.00), ('Monitor 24', 850.00),
('Cadeira Ergonomica', 1100.00), ('Fone Bluetooth', -89.90), -- [Valor Inválido]
('Webcam Full HD', 200.00), ('Pad XL', 60.00), ('Suporte Monitor', 90.00),
('Hub USB-C', 150.00), ('Mesa Digitalizadora', 400.00);

-- Inserindo Vendas (100 registros)
INSERT INTO vendas (id_cliente, id_produto, quantidade, valor_total, data_venda)
SELECT 
    floor(random() * 28 + 1)::int,
    floor(random() * 10 + 1)::int,
    floor(random() * 5 + 1)::int,
    150.00,
    '2026-03-01'::date
FROM generate_series(1, 96);

INSERT INTO vendas (id_cliente, id_produto, quantidade, valor_total, data_venda) VALUES
(5, 2, 2, 240.00, NULL),        -- [Dado Vazio]
(8, 1, -3, 750.00, '2026-03-02'),-- [Valor Inválido]
(12, 1, 1, 9999.00, '2026-03-03'),-- [Inconsistência]
(1, 1, 1, 250.00, '2026-03-01'); -- [Duplicidade]