 -- compose data with next 1,5 year (i.e. current year and 1/2 next year) quarters periods date including:
 -- start quarter period date / end quater period date /quater ID in year / quater sequence number ID report
  WITH RECURSIVE 
    qtrange(x) AS (SELECT 0 UNION ALL
                   SELECT (x+3) FROM qtrange
                   LIMIT 7)
    select   
    ' start_date ','end_date','qtyear_id','qtlist_id1','qtlist_id2','qtlist_id3','qtlist_id4','qtlist_id5','qtlist_id6','qtlist_id7'
    UNION             
    select                
      date('now','start of year',(qtrange.x)||' months','0 day') as start_date, 
      date('now','start of year', (qtrange.x+3) ||' months','-1 day') as end_date,
      'Q'||(substr(date('now','start of year', (qtrange.x+3) ||' months','-1 day'),6,2)/3) as qtyear_id,
      case(qtrange.x/3-0) when(0) then 1 else 0 end qtlist_id_1,
      case(qtrange.x/3-1) when(0) then 1 else 0 end qtlist_id_2,
      case(qtrange.x/3-2) when(0) then 1 else 0 end qtlist_id_3,
      case(qtrange.x/3-3) when(0) then 1 else 0 end qtlist_id_4,
      case(qtrange.x/3-4) when(0) then 1 else 0 end qtlist_id_5,
      case(qtrange.x/3-5) when(0) then 1 else 0 end qtlist_id_6,
      case(qtrange.x/3-6) when(0) then 1 else 0 end qtlist_id_7
    FROM qtrange
    UNION
    select
      '0000-00-00', date('now','start of year',(qtrange.x)||' months','-1 day'),'n/a',
      0,0,0,0,0,0,0
      FROM qtrange
	    where x=0
    UNION
    select
      date('now','start of year', (qtrange.x+3) ||' months','+1 day'),'9999-12-31','n/a',
      0,0,0,0,0,0,0
      FROM qtrange
	    where x = 18
    ;
