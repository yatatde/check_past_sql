-- compose data with next 1,5 year quarters periods (=7 periods) including:
-- start quarter period date / end quater period date /quater ID in year / quater sequence number ID report
WITH RECURSIVE
    qtrange (x) AS (
        SELECT 0
        UNION ALL
        SELECT (x + 3)
        FROM qtrange
        LIMIT 7
    )
select
    "Quater start date" as c1,
    "Quater end date" as c2,
    "Quater id per year" as c3,
    "Quater id per report: 1" as c4,
    "Quater id per report: 2" as c5,
    "Quater id per report: 3" as c6,
    "Quater id per report: 4" as c7,
    "Quater id per report: 5" as c8,
    "Quater id per report: 6" as c9,
    "Quater id per report: 7" as c10
UNION all
select
    date(
        'now',
        'start of year',
        concat(qtrange.x, ' months'),
        '0 day'
    ) as start_date,
    date(
        'now',
        'start of year',
        concat((qtrange.x + 3), ' months'),
        '-1 day'
    ) as end_date,
    'Q' || (
        substr(
            date(
                'now',
                'start of year',
                (qtrange.x + 3) || ' months',
                '-1 day'
            ),
            6,
            2
        ) / 3
    ) as qtyear_id,
    case (qtrange.x / 3 -0)
        when (0) then qtrange.x / 3 + 1
        else 0
    end,
    --id_1
    case (qtrange.x / 3 -1)
        when (0) then qtrange.x / 3 + 1
        else 0
    end,
    --id_2
    case (qtrange.x / 3 -2)
        when (0) then qtrange.x / 3 + 1
        else 0
    end,
    --id_3
    case (qtrange.x / 3 -3)
        when (0) then qtrange.x / 3 + 1
        else 0
    end,
    --id_4
    case (qtrange.x / 3 -4)
        when (0) then qtrange.x / 3 + 1
        else 0
    end,
    --id_5
    case (qtrange.x / 3 -5)
        when (0) then qtrange.x / 3 + 1
        else 0
    end,
    --id_6
    case (qtrange.x / 3 -6)
        when (0) then qtrange.x / 3 + 1
        else 0
    end --id_7
FROM qtrange
UNION all
select '0000-00-00', date(
        'now', 'start of year', (qtrange.x) || ' months', '-1 day'
    ), 'na', 0, 0, 0, 0, 0, 0, 0
FROM qtrange
where
    x = 0
UNION all
select date(
        'now', 'start of year', (qtrange.x + 3) || ' months', '+1 day'
    ), '9999-12-31', 'na', 0, 0, 0, 0, 0, 0, 0
FROM qtrange
where
    x = 18;