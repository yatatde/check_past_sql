-----------------------------------------  SQLITE ----------------------------------------------------
-- CUSTGOODS
-- goods_id,customer_id,goods_customer_id,goods_type,goods_weight,
-- CUSTGOODS
CREATE TABLE IF NOT EXISTS CUSTGOODS (
    goods_id          integer  PRIMARY KEY   
   ,customer_id       integer    NOT NULL
   ,goods_customer_id integer    NOT NULL
   ,goods_type        text       NOT NULL
   ,goods_weight      integer    NOT NULL
   );