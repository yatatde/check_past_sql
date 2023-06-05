-----------------------------------------  SQLITE ----------------------------------------------------
-- SYSTABLES
CREATE TABLE IF NOT EXISTS SYSTABLES (
    id integer  PRIMARY KEY  
   ,NAME        text    NOT NULL
   ,CREATOR     text    NOT NULL
   ,TYPE        text    NOT NULL
   );