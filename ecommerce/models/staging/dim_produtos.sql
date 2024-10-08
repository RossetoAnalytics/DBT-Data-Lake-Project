WITH produtos AS(
    SELECT *
    FROM{{source('raw', 'produtos')}}
),

dim_produtos AS(
    SELECT
        cast(product_id AS INT) as id_produto,
        name AS nome_produto,
        CAST(price AS FLOAT) AS preco_produto,
        current_timestamp AS dt_processamento
    FROM produtos
)

select * from
dim_produtos