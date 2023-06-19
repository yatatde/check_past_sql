-----------------------------------------  SQLITE ----------------------------------------------------
-- SYSTABAUTH
CREATE TABLE IF NOT EXISTS SYSTABAUTH (
   id integer  PRIMARY KEY   
   ,GRANTEES    text NOT NULL
   ,TCREATOR    text NOT NULL
   ,TTNAME      text NOT NULL
   ,SELECTAUTH  text NOT NULL
   ,INSERTAUTH  text NOT NULL
   ,UPDATEAUTH  text NOT NULL
   ,DELETEAUTH  text NOT NULL
   );