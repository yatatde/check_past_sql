--- AGGREGATION ---  Partitioning with row_number function
with suppl(preffix, header1, header2, suffix, row_delimeter) as (select 
                                          substr('|       |            |           |             |             ',1,48)
                                          ," goods_id| customer_id| goods_type| goods_weight"
                                          ," goods_id| customer_id| goods_type| goods_weight| row number on goods_weight"
                                          ,substr('               ',1,15)
                                          ,"--------------------------------------------------------------------------")
---- source data   
select s.row_delimeter from suppl s
union all
select 'Input q4 DATA ==>' 
union all
select s.header1 from suppl s
union all
select substr(goods_id||s.suffix,1,length('goods_id'))||'| '|| 
       substr(customer_id||s.suffix,1,length('customer_id'))||'| '|| 
       substr(goods_type||s.suffix,1,length('goods_type'))||'| '|| 
       substr(goods_weight||s.suffix,1,length('goods_weight'))
from CUSTGOODS, suppl s 
union all
----- selected data  
select s.row_delimeter from suppl s
union all
select 'Result q4 DATA ==>' 
union all                                                                            
select s.header2 from suppl s
union all
select (s.preffix||' partioned with goods_type  ') from suppl s
union all
select substr(goods_id||s.suffix,1,length('goods_id'))||'| '|| 
       substr(customer_id||s.suffix,1,length('customer_id'))||'| '|| 
       substr(goods_type||s.suffix,1,length('goods_type'))||'| '||
       substr(goods_weight||s.suffix,1,length('goods_weight'))||'| '||
      (ROW_NUMBER() 
            OVER (partition by 
            goods_type 
            order BY goods_weight)) rn  
FROM CUSTGOODS, suppl s  
union all select "--- generated at " || CURRENT_TIME ||', ' || CURRENT_DATE 