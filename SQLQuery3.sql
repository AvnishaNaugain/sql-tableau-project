SELECT 
    Ship_Mode,
    Region,
    COUNT(Order_ID) AS total_orders,
    ROUND(AVG(Discount), 2) AS avg_discount,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit)/SUM(Sales)*100, 2) AS profit_margin_pct
FROM Superstore
GROUP BY Ship_Mode, Region
ORDER BY total_profit DESC;