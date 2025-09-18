--- AGGREGATION --- Partitioning with row_number function
with header1( col1, col2, col3, col4, col5) as 
	(select " goods_id", "customer_id", "goods_type", "goods_weight", "comment")
   ,header2( col1, col2, col3, col4, col5) as 
	 (select " goods_id", "customer_id", "goods_type", "goods_weight", "row number on goods_weight partioned with goods_type ")
---- source data  
select "SubTab","2.1. A table with processing input data ", " ",  " ", " " 
union all
select h1.col1, h1.col2, h1.col3,  h1.col4 ,  h1.col5 from header1 h1
union all
select goods_id, 
    customer_id,
    goods_type,
    goods_weight,
	"An input data for an example query"
from CUSTGOODS
union all
select "SubTab","2.2. A table with results data ", " ",  " ", " " 
union all
select h2.col1, h2.col2, h2.col3, h2.col4, h2.col5 from header2 h2
union all
select goods_id, 
    customer_id,
    goods_type,
    goods_weight,
   (ROW_NUMBER() 
      OVER (partition by 
      goods_type 
      order BY goods_weight)) rn 
FROM CUSTGOODS 
--union all select "--- generated at " || strftime( datetime(current_timestamp, 'localtime'))