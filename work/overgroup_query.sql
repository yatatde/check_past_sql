SELECT  goods_id, customer_id, goods_type,
      (ROW_NUMBER() OVER (partition by (customer_id > 2 and goods_id > 4 ) order BY goods_weight)) RN  
FROM CUSTGOODS d 