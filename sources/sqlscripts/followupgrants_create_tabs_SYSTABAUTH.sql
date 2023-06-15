-----------------------------------------  SQLITE ----------------------------------------------------
-- SYSTABAUTH
CREATE TABLE IF NOT EXISTS SYSTABAUTH (
    id          integer  PRIMARY KEY   
   ,GRANTOR     text NOT NULL
   ,GRANTEE     text NOT NULL
   ,GRANTEETYPE text NOT NULL
   ,TCREATOR    text NOT NULL
   ,TTNAME      text NOT NULL
   ,ALTERAUTH   text NOT NULL
   ,DELETEAUTH  text NOT NULL
   ,INDEXAUTH   text NOT NULL
   ,INSERTAUTH  text NOT NULL
   ,SELECTAUTH  text NOT NULL
   ,UPDATEAUTH  text NOT NULL
   );