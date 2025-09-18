-------------------------------------  SQLITE ---------------------------------------------------
-- TABLES_GRANTS_EXIST contains processing groups for the requered access check to generate commands 
-- TABLES_GRANTS_MUST_HAVE contains set up for grants of processing groups for generating commands   
-- GRANTEES - group to be granted                                                                    
-- SELECTAUTH, UPDATEAUTH, DELETEAUTH, INSERTAUTH - what should be granted                           
-- TABLEPREFIX - prefix of table's name or whole table's name for which granted                      
with TABLES_GRANTS_MUST_HAVE                                                                          
  (GRANTEES, TABLEPREFIX, SELECTAUTH, UPDATEAUTH, DELETEAUTH, INSERTAUTH)                            
as
 (select 'CRANTEE_MUST_A', 'TABPR',    'SELECT',         '',       '',       '' from SYSDUMMY1 union
  select 'CRANTEE_MUST_A', 'TABPRM',   'SELECT',   'UPDATE', 'DELETE', 'INSERT' from SYSDUMMY1 union
  select 'CRANTEE_MUST_A', 'TABPRADMT','SELECT',   'UPDATE', 'DELETE', 'INSERT' from SYSDUMMY1 union
  select 'CRANTEE_MUST_B', 'TABPR',    'SELECT',         '',       '',       '' from SYSDUMMY1 
--union
-- select 'CRANTEE_MUST_C', 'TABPR',    'SELECT',        '',       '',       '' from SYSDUMMY1 
--union 
-- select 'CRANTEE_ADM' ,   'TABPR',    'SELECT',        '',       '',       '' from SYSDUMMY1 
--union 
-- select 'CRANTEE_MUST_E', 'TABPR',          '',        '',       '',       '' from SYSDUMMY1 
  ),
--  TABLES_GRANTS_MUST_HAVE 
--  (GRANTEES, TABLEPREFIX, SELECTAUTH, UPDATEAUTH, DELETEAUTH, INSERTAUTH) 
--as
--  (select GRANTEES, TABLEPREFIX, MAX(SELECTAUTH), MAX(UPDATEAUTH), MAX(DELETEAUTH), MAX(INSERTAUTH)
--   from TABLES_GRANTS_REQUIRED
--   group by GRANTEES, TABLEPREFIX
--  ),
  TABLES_GRANTS_EXIST
  (TCREATOR, TTNAME, GRANTEES, SELECTAUTH, INSERTAUTH, UPDATEAUTH, DELETEAUTH)
as 
  (select STABAUTH.TCREATOR, STABAUTH.TTNAME, STABAUTH.GRANTEES,
    case when max(STABAUTH.SELECTAUTH)  in ('Y','G')
      then 'SELECT' else ''
    end as SELECTAUTH,
    case when max(STABAUTH.INSERTAUTH)  in ('Y','G')
      then 'INSERT' else ''
    end as INSERTAUTH,
    case when max(STABAUTH.UPDATEAUTH)  in ('Y','G')
      then 'UPDATE' else ''
    end as UPDATEAUTH,
    case when max(STABAUTH.DELETEAUTH)  in ('Y','G')
      then 'DELETE' else ''
    end as DELETEAUTH
  from SYSTABLES STAB, SYSTABAUTH STABAUTH
    where 
        STAB.TYPE    =  'T'
--    and STAB.NAME  like 'TABPR%'
      and STAB.CREATOR =  STABAUTH.TCREATOR
      and STAB.NAME    =  STABAUTH.TTNAME
      and STAB.CREATOR =  'CRANTEE_ADM'
    group by STABAUTH.TCREATOR, STABAUTH.TTNAME, STABAUTH.GRANTEES
  )
------- GENERATE REVOKE STATEMENTS
select " A list of generated SQL statements on GRANTS modifications reflected TABLES_GRANTS_MUST_HAVE requirements. A processing time stamp: " || strftime( datetime(current_timestamp, 'localtime')) from SYSDUMMY1 as command
UNION
select  (' REVOKE ' 
  || rtrim
      (case when (TG_EXIST.SELECTAUTH <> '' and TG_MUST_HAVE.SELECTAUTH = '') 
          then TG_EXIST.SELECTAUTH || ', ' else ''
      end ||
      case when (TG_EXIST.DELETEAUTH <> ''  and TG_MUST_HAVE.DELETEAUTH = '') 
          then TG_EXIST.DELETEAUTH || ', ' else ''
      end ||
      case when (TG_EXIST.INSERTAUTH <> ''  and TG_MUST_HAVE.INSERTAUTH = '') 
          then TG_EXIST.INSERTAUTH || ', ' else ''
      end ||
      case when (TG_EXIST.UPDATEAUTH <> ''  and TG_MUST_HAVE.UPDATEAUTH = '') 
          then TG_EXIST.UPDATEAUTH            else ''
      end,' ,')
  || ' ON TABLE ' || trim(TG_EXIST.TTNAME) 
  || ' from '     || TG_MUST_HAVE.GRANTEES || ';') as command 
from TABLES_GRANTS_MUST_HAVE as TG_MUST_HAVE inner join TABLES_GRANTS_EXIST as TG_EXIST
  on   
        instr(trim(TG_EXIST.TTNAME),trim(TG_MUST_HAVE.TABLEPREFIX))>0  
    and TG_MUST_HAVE.GRANTEES    = TG_EXIST.GRANTEES 
    and TG_MUST_HAVE.TABLEPREFIX = (select max(MH.TABLEPREFIX) 
                                    from TABLES_GRANTS_MUST_HAVE as MH 
                                      where 
                                            instr(trim(TG_EXIST.TTNAME),trim(MH.TABLEPREFIX))>0
                                        and TG_EXIST.GRANTEES = MH.GRANTEES 
                                        group by MH.GRANTEES)   
    and  ((TG_MUST_HAVE.SELECTAUTH = '' and TG_EXIST.SELECTAUTH <> '') 
        or(TG_MUST_HAVE.DELETEAUTH = '' and TG_EXIST.DELETEAUTH <> '') 
        or(TG_MUST_HAVE.INSERTAUTH = '' and TG_EXIST.INSERTAUTH <> '') 
        or(TG_MUST_HAVE.UPDATEAUTH = '' and TG_EXIST.UPDATEAUTH <> ''))
---1---- GENERATE GRANT STATEMENTS
union 
select  (' GRANT ' 
  || rtrim
      (case when (TG_EXIST.SELECTAUTH = '' and TG_MUST_HAVE.SELECTAUTH <> '')
          then TG_MUST_HAVE.SELECTAUTH || ', ' else '' end ||
      case when (TG_EXIST.DELETEAUTH = '' and TG_MUST_HAVE.DELETEAUTH <> '') 
          then TG_MUST_HAVE.DELETEAUTH || ', ' else '' end ||
      case when (TG_EXIST.INSERTAUTH = '' and TG_MUST_HAVE.INSERTAUTH <> '') 
          then TG_MUST_HAVE.INSERTAUTH || ', ' else '' end ||
      case when (TG_EXIST.UPDATEAUTH = '' and TG_MUST_HAVE.UPDATEAUTH <> '') 
          then TG_MUST_HAVE.UPDATEAUTH         else '' end,' ,')
  || ' ON TABLE '
  || rtrim (TG_EXIST.TTNAME) || ' TO ' ||
            TG_MUST_HAVE.GRANTEES || ';') as command 
from  TABLES_GRANTS_EXIST as TG_EXIST inner join TABLES_GRANTS_MUST_HAVE as TG_MUST_HAVE
  on
        TG_MUST_HAVE.GRANTEES = TG_EXIST.GRANTEES 
    and  instr(trim(TG_EXIST.TTNAME),trim(TG_MUST_HAVE.TABLEPREFIX))>0
    and  ((TG_MUST_HAVE.SELECTAUTH <> '' and TG_EXIST.SELECTAUTH = '') 
       or (TG_MUST_HAVE.DELETEAUTH <> '' and TG_EXIST.DELETEAUTH = '') 
       or (TG_MUST_HAVE.INSERTAUTH <> '' and TG_EXIST.INSERTAUTH = '') 
       or (TG_MUST_HAVE.UPDATEAUTH <> '' and TG_EXIST.UPDATEAUTH = ''))
    and TG_MUST_HAVE.TABLEPREFIX = (select  max(MH.TABLEPREFIX) 
                                    from TABLES_GRANTS_MUST_HAVE as MH 
                                      where 
                                            instr(trim(TG_EXIST.TTNAME),trim(MH.TABLEPREFIX))>0 
                                        and TG_EXIST.GRANTEES = MH.GRANTEES 
                                    group by MH.GRANTEES)   
union
---2---- GENERATE GRANT STATEMENTS
select  (' GRANT ' ||
  trim(
    (case when (TG_MUST_HAVE.SELECTAUTH <> '' )   
         then TG_MUST_HAVE.SELECTAUTH   else '' 
	  end ||
     case when (TG_MUST_HAVE.DELETEAUTH <> '')    
         then ', '||TG_MUST_HAVE.DELETEAUTH  else '' 
	  end ||
    case when (TG_MUST_HAVE.INSERTAUTH <> '')     
         then ', '||TG_MUST_HAVE.INSERTAUTH  else '' 
  	end ||
	  case when   (TG_MUST_HAVE.UPDATEAUTH <> '' )     
        then ', '||TG_MUST_HAVE.UPDATEAUTH         else '' 
		end),', ')
  || ' ON TABLE ' || TG_EXIST.TTNAME 
  || ' TO ' || TG_MUST_HAVE.GRANTEES || ';') as command 
from TABLES_GRANTS_EXIST as TG_EXIST inner join  TABLES_GRANTS_MUST_HAVE as TG_MUST_HAVE 
  on    
    instr(trim(TG_EXIST.TTNAME), trim(TG_MUST_HAVE.TABLEPREFIX))>0
    and TG_MUST_HAVE.TABLEPREFIX = (select max(MH.TABLEPREFIX) 
                                    from TABLES_GRANTS_MUST_HAVE as MH 
                                      where 
                                            instr(trim(TG_EXIST.TTNAME),trim(MH.TABLEPREFIX))>0
                                        and TG_MUST_HAVE.GRANTEES = MH.GRANTEES 
                                    group by MH.GRANTEES)   
  group by TG_EXIST.TTNAME, 
      TG_MUST_HAVE.GRANTEES, TG_MUST_HAVE.TABLEPREFIX, 
      TG_MUST_HAVE.SELECTAUTH, TG_MUST_HAVE.DELETEAUTH, TG_MUST_HAVE.INSERTAUTH ,TG_MUST_HAVE.UPDATEAUTH
	  having  sum(instr(trim(TG_EXIST.GRANTEES),trim(TG_MUST_HAVE.GRANTEES))) = 0
	    and NOT (  TG_MUST_HAVE.SELECTAUTH = '' 	
			         and TG_MUST_HAVE.DELETEAUTH = '' 	
			         and TG_MUST_HAVE.INSERTAUTH = '' 
			         and TG_MUST_HAVE.UPDATEAUTH = '') 
