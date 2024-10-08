SELECT
    tipo_loja,
    SUM(total_venda) AS receita_total
FROM {{ ref('agg_ecommerce') }}
GROUP BY tipo_loja
ORDER BY receita_total DESC