-- The pupose of query  - to review existing grantees privileges 
-- against grantees privileges allowed. 
-- The review report generated with review status indicating if existing granted 
-- privilegious:  
--      is OK (i.e. meet GRANTEES_PRIVILEGES_ALLOWED list)      
--      or NOTOK (i.e. does not meet GRANTEES_PRIVILEGES_ALLOWED list)
-- The review report has format like csv and can be imported into MS EXEL  
WITH 
TABLES_TO_CHECK
(TSNAME, TABNAME, DBNAME, CREATOR) --, LABEL) 
AS (SELECT TSNAME, NAME, DBNAME, CREATOR  --, LABEL 
      FROM SYSTABLES
        WHERE TYPE = "T"
          AND DBNAME LIKE "%TESTDB%"),
GRANTEES_PRIVILEGES_ALLOWED -- the part should be updated with needed data on grants allowed 
(CHECK_GROUPS, ALTERAUTH, DELETEAUTH, INDEXAUTH, INSERTAUTH, SELECTAUTH, UPDATEAUTH)
AS (SELECT "CHECK_GROUP_1", "G", "G", "G", "G", "G", "G"
    FROM SYSDUMMY1 UNION
    SELECT "CHECK_GROUP_2", " ", " ", " ", " ", "Y", " "
    FROM SYSDUMMY1 UNION
    SELECT "CHECK_GROUP_3", " ", "Y ", " ", "Y", "Y", "Y"
    FROM SYSDUMMY1 UNION
    SELECT "CHECK_GROUP_4", "G", "G", "G", "G", "G", "G"
    FROM SYSDUMMY1 UNION
    SELECT "CHECK_GROUP_5", " ", " ", " ", " ", "Y", " "
    FROM SYSDUMMY1 UNION
    SELECT "CHECK_GROUP_6", " ", "Y ", " ", "Y", "Y", "Y"
    FROM SYSDUMMY1 UNION
    SELECT "CHECK_GROUP_7", "G", "G", "G", "G", "G", "G"
    FROM SYSDUMMY1 UNION
    SELECT "CHECK_GROUP_8", " ", "Y ", " ", "Y", "Y", "Y"
    FROM SYSDUMMY1 UNION
    SELECT "CHECK_GROUP_9", " ", " ", " ", " ", "Y", " "
    FROM SYSDUMMY1),
GRANTEES_PRIVILEGES_EXIST
(GRANTEE,TTNAME,ALTERAUTH, DELETEAUTH, INDEXAUTH, INSERTAUTH, SELECTAUTH, UPDATEAUTH) 
AS (SELECT GRANTEE, TTNAME, MAX(ALTERAUTH), MAX(DELETEAUTH), MAX(INDEXAUTH),
           MAX(INSERTAUTH), MAX(SELECTAUTH), MAX(UPDATEAUTH)
    FROM SYSTABAUTH
      WHERE GRANTEE IN 
            (SELECT CHECK_GROUPS FROM GRANTEES_PRIVILEGES_ALLOWED)
      GROUP BY GRANTEE, TTNAME)
-- header of the report
SELECT '" GRANTOR',' GRANTEE',' TTNAME', ' ALTERAUTH', ' DELETEAUTH', ' INDEXAUTH',' INSERTAUTH', ' SELECTAUTH',
        ' UPDATEAUTH',' Review status'AS OK_STATUS,' Review TIMESTAMP' AS QUERY_TS FROM SYSDUMMY1 
  UNION
-- content data of the report start
SELECT SA.GRANTOR, SA.GRANTEE, SA.TTNAME ,SA.ALTERAUTH, SA.DELETEAUTH, SA.INDEXAUTH ,SA.INSERTAUTH, 
  SA.SELECTAUTH, SA.UPDATEAUTH , "not_OK" AS OK_STATUS, CURRENT_TIMESTAMP AS QUERY_TS 
  FROM SYSTABAUTH SA, TABLES_TO_CHECK TTC, GRANTEES_PRIVILEGES_ALLOWED GPTC, GRANTEES_PRIVILEGES_EXIST GF
    WHERE 
          SA.TTNAME = TTC.TABNAME
      AND NOT SA.GRANTEETYPE = "P" -- excluded applications PLAN / PACKAGES
      AND SA.GRANTEE = GPTC.CHECK_GROUPS
      AND GF.TTNAME = TTC.TABNAME
      AND GF.GRANTEE = GPTC.CHECK_GROUPS
      AND NOT (GF.ALTERAUTH, GF.DELETEAUTH, GF.INDEXAUTH, GF.INSERTAUTH, GF.SELECTAUTH, GF.UPDATEAUTH) = 
              (GPTC.ALTERAUTH, GPTC.DELETEAUTH, GPTC.INDEXAUTH, GPTC.INSERTAUTH, GPTC.SELECTAUTH, GPTC.UPDATEAUTH)
UNION
SELECT SA.GRANTOR, SA.GRANTEE, SA.TTNAME, SA.ALTERAUTH, SA.DELETEAUTH, SA.INDEXAUTH, SA.INSERTAUTH, 
  SA.SELECTAUTH, SA.UPDATEAUTH, "OK" AS OK_STATUS, CURRENT_TIMESTAMP AS QUERY_TS 
  FROM SYSTABAUTH SA, TABLES_TO_CHECK TTC, GRANTEES_PRIVILEGES_ALLOWED GPTC, GRANTEES_PRIVILEGES_EXIST GF
    WHERE 
      SA.TTNAME = TTC.TABNAME
      AND NOT SA.GRANTEETYPE = "P"
      AND SA.GRANTEE = GPTC.CHECK_GROUPS
      AND GF.TTNAME  = TTC.TABNAME
      AND GF.GRANTEE = GPTC.CHECK_GROUPS
      AND (GF.ALTERAUTH, GF.DELETEAUTH, GF.INDEXAUTH, GF.INSERTAUTH, GF.SELECTAUTH, GF.UPDATEAUTH)
         =(GPTC.ALTERAUTH, GPTC.DELETEAUTH, GPTC.INDEXAUTH, GPTC.INSERTAUTH, GPTC.SELECTAUTH, GPTC.UPDATEAUTH)
ORDER BY 10,2,3
-- content data of the report end