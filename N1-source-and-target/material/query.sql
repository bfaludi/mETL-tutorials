WITH

ordered_names AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY 
                country_code
            ORDER BY
                population DESC NULLS LAST
        ) AS "idx"
    FROM
        names
    WHERE
        type = 'lastname'
)

SELECT
    *
FROM
    ordered_names
WHERE
    idx < 100
;