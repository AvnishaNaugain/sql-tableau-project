SELECT 
    Region,
    Segment,
    COUNT(Order_ID) AS total_orders,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(AVG(Discount), 2) AS avg_discount
FROM Superstore
WHERE Profit < 0
GROUP BY Region, Segment
ORDER BY total_profit ASC;