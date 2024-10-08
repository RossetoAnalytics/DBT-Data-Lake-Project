SELECT
    id_cliente,
    nome_cliente,
    SUM(total_venda) AS receita_total
FROM {{ ref('agg_ecommerce') }}
GROUP BY id_cliente, nome_cliente
ORDER BY receita_total DESC
LIMIT 15