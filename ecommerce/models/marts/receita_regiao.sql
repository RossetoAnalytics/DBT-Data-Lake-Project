SELECT
    cidade AS regiao,
    SUM(total_venda) AS receita_total
FROM {{ ref('agg_ecommerce') }}
GROUP BY cidade
ORDER BY receita_total DESC