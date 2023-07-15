DROP TABLE IF EXISTS dim_date;

CREATE TABLE dim_date
(
    datekey integer NOT NULL,
    date timestamp without time zone,
    fulldate character(10) COLLATE pg_catalog."default",
    dayofmonth character varying(2) COLLATE pg_catalog."default",
    dayname character varying(9) COLLATE pg_catalog."default",
    dayofweek character(1) COLLATE pg_catalog."default",
    dayofweekinmonth character varying(2) COLLATE pg_catalog."default",
    dayofweekinyear character varying(2) COLLATE pg_catalog."default",
    dayofquarter character varying(3) COLLATE pg_catalog."default",
    dayofyear character varying(3) COLLATE pg_catalog."default",
    weekofmonth character varying(1) COLLATE pg_catalog."default",
    weekofquarter character varying(2) COLLATE pg_catalog."default",
    weekofyear character varying(2) COLLATE pg_catalog."default",
    month character varying(2) COLLATE pg_catalog."default",
    monthname character varying(9) COLLATE pg_catalog."default",
    monthofquarter character varying(2) COLLATE pg_catalog."default",
    quarter character(1) COLLATE pg_catalog."default",
    quartername character varying(9) COLLATE pg_catalog."default",
    year character(4) COLLATE pg_catalog."default",
    yearname character(7) COLLATE pg_catalog."default",
    monthyear character(10) COLLATE pg_catalog."default",
    mmyyyy character(6) COLLATE pg_catalog."default",
    firstdayofmonth date NOT NULL,
    lastdayofmonth date NOT NULL,
    firstdayofquarter date NOT NULL,
    lastdayofquarter date NOT NULL,
    firstdayofyear date NOT NULL,
    lastdayofyear date NOT NULL,
    CONSTRAINT dim_date_pkey PRIMARY KEY (datekey)
);

