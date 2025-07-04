# Uso de tablas particionadas

## Ejercicio 1. Creando una tabla regular en el TBS_REGULAR

```
SQL> CREATE TABLESPACE TBS_REGULAR
  2  DATAFILE 'C:\APP\KRR\PRODUCT\21C\ORADATA\XE\XEPDB1\DF_COMPROBANTES_REGULAR.DBF'
  3  SIZE 100M;

Tablespace created.

SQL>
SQL> CREATE TABLE VENTASREGULAR
  2  (ID NUMBER(10),
  3  ORIGEN VARCHAR2(20),
  4  FECHA DATE default sysdate ) TABLESPACE TBS_REGULAR;

Table created.
```

## Ejercicio 2: Insertando 4 millones de registros

```
NSERT INTO VENTASREGULAR
SELECT LEVEL, 'ASIA', SYSDATE
FROM DUAL CONNECT BY LEVEL <= 2000000;
INSERT INTO VENTASREGULAR
SELECT LEVEL, 'EUROPA', SYSDATE
FROM DUAL CONNECT BY LEVEL <=2000000;
```

En una primera instancia los ultimos 2 millones no caben en el datafile,
por lo que se redimensiona a 200m.

```
SQL> alter database datafile 'C:\APP\KRR\PRODUCT\21C\oradata\xe\xepdb1\df_comprobantes_regular.dbf' resize 200M; 

Database altered.

SQL> INSERT INTO VENTASREGULAR
  2  SELECT LEVEL, 'EUROPA', SYSDATE
  3  FROM DUAL CONNECT BY LEVEL <=2000000;

2000000 rows created.
```
## Ejercicio 3: Verificación

``` 
SQL> SELECT COUNT(*) FROM VENTASREGULAR;

  COUNT(*)
----------
   4000000
```

## Ejercicio 4: Obteniendo el plan de ejecución

```
EXPLAIN PLAN
FOR
SELECT * FROM VENTASREGULAR
WHERE ORIGEN = 'ASIA';

PLAN_TABLE_OUTPUT
--------------------------------------------------------------------------------
Plan hash value: 2646100163

--------------------------------------------------------------------------------
---

| Id  | Operation         | Name          | Rows  | Bytes | Cost (%CPU)| Time
  |

--------------------------------------------------------------------------------
---


PLAN_TABLE_OUTPUT
--------------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |               |   156 |  5304 |  3885   (2)| 00:00:0
1 |

|*  1 |  TABLE ACCESS FULL| VENTASREGULAR |   156 |  5304 |  3885   (2)| 00:00:0
1 |

--------------------------------------------------------------------------------
---


Predicate Information (identified by operation id):

PLAN_TABLE_OUTPUT
--------------------------------------------------------------------------------
---------------------------------------------------

   1 - filter("ORIGEN"='ASIA')

Note
-----
   - dynamic statistics used: dynamic sampling (level=2)

17 rows selected.
```

## Ejercicio 5: Creación de TBS

```

SQL> CREATE TABLESPACE TBS_ASIA
  2  DATAFILE 'C:/app/krr/product/21c/oradata/xe/xepdb1/DF_COMPROBANTES_ASIA.DBF'
  3  SIZE 100M;

Tablespace created.

SQL>
SQL> CREATE TABLESPACE TBS_EUROPA
  2  DATAFILE 'C:/app/krr/product/21c/oradata/xe/xepdb1/DF_COMPROBANTES_EUROPA.DBF'
  3  SIZE 100M;

Tablespace created.

SQL>
SQL> CREATE TABLESPACE TBS_AL
  2  DATAFILE 'C:/app/krr/product/21c/oradata/xe/xepdb1/DF_COMPROBANTES_AL.DBF'
  3  SIZE 100M;

Tablespace created.

SQL>
SQL> CREATE TABLESPACE TBS_OTROS
  2  DATAFILE 'C:/app/krr/product/21c/oradata/xe/xepdb1/DF_COMPROBANTES_OTROS.DBF'
  3  SIZE 100M;

Tablespace created.
```

## Ejercicio 6: Crear tablas particionadas por lista

```
SQL> CREATE TABLE Ventas
  2  (ID NUMBER(10),
  3  ORIGEN VARCHAR2(20),
  4  FECHA DATE default sysdate )
  5  PARTITION BY LIST( ORIGEN)
  6  (PARTITION ventas_ASIA VALUES('ASIA') tablespace TBS_ASIA,
  7  PARTITION ventas_EUROPA VALUES ('EUROPA') tablespace TBS_EUROPA,
  8  PARTITION ventas_AL VALUES ('AL') tablespace TBS_AL,
  9  PARTITION ventas_otros VALUES(DEFAULT) tablespace TBS_OTROS );

Table created.
```

## Ejercicio 7: Insertando datos en tablas particionadas
Inserción de 500 mil registros en dos de las particiones creadas
```
INSERT INTO VENTAS
SELECT LEVEL, 'ASIA', SYSDATE
FROM DUAL CONNECT BY LEVEL <= 500000;

INSERT INTO VENTAS
SELECT LEVEL, 'EUROPA', SYSDATE
FROM DUAL CONNECT BY LEVEL <= 500000;
```

```
SQL> INSERT INTO VENTAS
  2  SELECT LEVEL, 'ASIA', SYSDATE
  3  FROM DUAL CONNECT BY LEVEL <= 500000;

500000 rows created.

SQL>
SQL> INSERT INTO VENTAS
  2  SELECT LEVEL, 'EUROPA', SYSDATE
  3  FROM DUAL CONNECT BY LEVEL <= 500000;

500000 rows created.
```

## Ejercicio 8: Query de tablas particionadas

```
// Todos los registros de la tabla
SELECT COUNT(*) FROM VENTAS;
// Registros de una partición
SELECT COUNT(*) FROM VENTAS PARTITION ( ventas_ASIA );
SELECT COUNT(*) FROM VENTAS PARTITION (ventas_EUROPA);
```
```
SQL> SELECT COUNT(*) FROM VENTAS;                          

  COUNT(*)
----------
   1000000

SQL> SELECT COUNT(*) FROM VENTAS PARTITION (ventas_ASIA); 

  COUNT(*)
----------
    500000

SQL> SELECT COUNT(*) FROM VENTAS PARTITION (ventas_EUROPA); 

  COUNT(*)
----------
    500000
```

## Ejercicio 9: 
