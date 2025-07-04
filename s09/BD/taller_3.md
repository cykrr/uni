# Taller 3: Tarea

1. Cree una tabla particionada para almacenar los datos de los clientes de un
banco, de acuerdo a la sucursal donde está inscrito el cliente. (asuma que el
banco tiene una sucursal en ‘Valparaíso’, otra en ‘Santiago’ y una tercera en
‘Concepción’). De cada cliente almacene un idCliente, el nombre, el código de la
sucursal del cliente y la fecha de nacimiento.


```sql
CREATE TABLESPACE TBS_VALPARAISO
    DATAFILE 'C:\app\krr\product\21c\oradata\xe\xepdb1\tbs_valparaiso.dbf' 
         SIZE 50M;

CREATE TABLESPACE TBS_SANTIAGO
    DATAFILE 'C:\app\krr\product\21c\oradata\xe\xepdb1\tbs_santiago.dbf'
         SIZE 50M;

CREATE TABLESPACE TBS_CONCEPCION
    DATAFILE 'C:\app\krr\product\21c\oradata\xe\xepdb1\tbs_concepcion.dbf'
         SIZE 50M;

CREATE TABLESPACE TBS_OTROS
    DATAFILE 'C:\app\krr\product\21c\oradata\xe\xepdb1\tbs_otros.dbf'
         SIZE 50M;

```


```
SQL> CREATE TABLESPACE TBS_VALPARAISO
  2      DATAFILE 'C:\app\krr\product\21c\oradata\xe\xepdb1\tbs_valparaiso.dbf'
  3           SIZE 50M;

Tablespace created.

SQL>
SQL> CREATE TABLESPACE TBS_SANTIAGO
  2      DATAFILE 'C:\app\krr\product\21c\oradata\xe\xepdb1\tbs_santiago.dbf'
  3           SIZE 50M;

Tablespace created.

SQL>
SQL> CREATE TABLESPACE TBS_CONCEPCION
  2      DATAFILE 'C:\app\krr\product\21c\oradata\xe\xepdb1\tbs_concepcion.dbf'
  3           SIZE 50M;

Tablespace created.

SQL> 
SQL> CREATE TABLESPACE TBS_OTROS                  
  2      DATAFILE 'C:\app\krr\product\21c\oradata\xe\xepdb1\tbs_otros.dbf'
  3           SIZE 50M;

Tablespace created.
```


```sql

CREATE TABLE Clientes (
    idCliente NUMBER(10),
    nombre VARCHAR2(100),
    codigoSucursal VARCHAR2(20),
    fechaNacimiento DATE
) PARTITION BY LIST (codigoSucursal)
(
    PARTITION clientes_valparaiso VALUES ('VALPARAISO') TABLESPACE TBS_VALPARAISO,
    PARTITION clientes_santiago VALUES ('SANTIAGO') TABLESPACE TBS_SANTIAGO,
    PARTITION clientes_concepcion VALUES ('CONCEPCION') TABLESPACE TBS_CONCEPCION,
    PARTITION clientes_otros VALUES (DEFAULT) TABLESPACE TBS_OTROS
);

Table created.
```

2. Muestre las particiones creadas

```
SELECT TABLE_NAME, PARTITION_NAME, HIGH_VALUE
FROM USER_TAB_PARTITIONS
WHERE TABLE_NAME = 'CLIENTES';

TABLE_NAME
--------------------------------------------------------------------------------
PARTITION_NAME
--------------------------------------------------------------------------------
HIGH_VALUE
--------------------------------------------------------------------------------
CLIENTES
CLIENTES_CONCEPCION
'CONCEPCION'

CLIENTES
CLIENTES_OTROS
DEFAULT

TABLE_NAME
--------------------------------------------------------------------------------
PARTITION_NAME
--------------------------------------------------------------------------------
HIGH_VALUE
--------------------------------------------------------------------------------

CLIENTES
CLIENTES_SANTIAGO
'SANTIAGO'

CLIENTES
CLIENTES_VALPARAISO

TABLE_NAME
--------------------------------------------------------------------------------
PARTITION_NAME
--------------------------------------------------------------------------------
HIGH_VALUE
--------------------------------------------------------------------------------
'VALPARAISO'
```

3. Inserte un millón de registros por cada partición

``` 
INSERT INTO CLIENTES (IDCLIENTE, NOMBRE, CODIGOSUCURSAL, FECHANACIMIENTO)
    SELECT LEVEL, DBMS_RANDOM.STRING('U', 10), 'VALPARAISO', SYSDATE FROM DUAL CONNECT BY LEVEL <= 1000000;


INSERT INTO CLIENTES (IDCLIENTE, NOMBRE, CODIGOSUCURSAL, FECHANACIMIENTO)
    SELECT LEVEL, DBMS_RANDOM.STRING('U', 10), 'SANTIAGO', SYSDATE FROM DUAL CONNECT BY LEVEL <= 1000000;

INSERT INTO CLIENTES (IDCLIENTE, NOMBRE, CODIGOSUCURSAL, FECHANACIMIENTO)
    SELECT LEVEL, DBMS_RANDOM.STRING('U', 10), 'CONCEPCION', SYSDATE FROM DUAL CONNECT BY LEVEL <= 1000000;
```

```
INSERT INTO CLIENTES (IDCLIENTE, NOMBRE, CODIGOSUCURSAL, FECHANACIMIENTO)
    SELECT LEVEL, DBMS_RANDOM.STRING('U', 10), 'CONCEPCION', SYSDATE FROM DUAL CONNECT BY LEVEL <= 1000000;
```

4. Muestre los 10 primeros clientes de la sucursal de Valparaíso

```
SELECT * 
FROM CLIENTES 
WHERE CODIGOSUCURSAL = 'VALPARAISO' 
AND ROWNUM <= 10;
```

5.  Comparación tabla de ejecución

Creamos tabla normal

```
CREATE TABLE ClientesRegular (
    idCliente NUMBER(10),
    nombre VARCHAR2(100),
    codigoSucursal VARCHAR2(20),
    fechaNacimiento DATE
);

```

Generamos plan regular 

```
EXPLAIN PLAN FOR SELECT * FROM CLIENTESREGULAR WHERE codigoSucursal='VALPARAISO';
SELECT * FROM TABLE (DBMS_XPLAN.DISPLAY);
```

```
LAN_TABLE_OUTPUT
--------------------------------------------------------------------------------
Plan hash value: 1492959430

--------------------------------------------------------------------------------
-----

| Id  | Operation         | Name            | Rows  | Bytes | Cost (%CPU)| Time
    |

--------------------------------------------------------------------------------
-----


PLAN_TABLE_OUTPUT
--------------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |                 |     1 |    86 |     2   (0)| 00:00
:01 |

|*  1 |  TABLE ACCESS FULL| CLIENTESREGULAR |     1 |    86 |     2   (0)| 00:00
:01 |

--------------------------------------------------------------------------------
-----


Predicate Information (identified by operation id):

PLAN_TABLE_OUTPUT
--------------------------------------------------------------------------------
---------------------------------------------------

   1 - filter("CODIGOSUCURSAL"='VALPARAISO')

Note
-----
   - dynamic statistics used: dynamic sampling (level=2)

17 rows selected.
```

Generamos plan para tabla particionada

```
EXPLAIN PLAN  FOR SELECT * FROM CLIENTES PARTITION ( CLIENTES_VALPARAISO );
SELECT * FROM TABLE (DBMS_XPLAN.DISPLAY);
```

```

PLAN_TABLE_OUTPUT
--------------------------------------------------------------------------------
Plan hash value: 1834176489

--------------------------------------------------------------------------------
------------------

| Id  | Operation             | Name     | Rows  | Bytes | Cost (%CPU)| Time
 | Pstart| Pstop |

--------------------------------------------------------------------------------
------------------


PLAN_TABLE_OUTPUT
--------------------------------------------------------------------------------
|   0 | SELECT STATEMENT      |          |  1268K|   103M|  2333  (30)| 00:00:01
 |       |       |

|   1 |  PARTITION LIST SINGLE|          |  1268K|   103M|  2333  (30)| 00:00:01
 |   KEY |   KEY |

|   2 |   TABLE ACCESS FULL   | CLIENTES |  1268K|   103M|  2333  (30)| 00:00:01
 |     1 |     1 |

--------------------------------------------------------------------------------
------------------

PLAN_TABLE_OUTPUT
--------------------------------------------------------------------------------


Note
-----
   - dynamic statistics used: dynamic sampling (level=2)

13 rows selected.
```


notamos que en el caso regular Oracle accede a la totalidad de la tabla buscando las coincidencias de codifoSucursal=VALPARAISO. Por otro lado la tabla particionada Se accede solo a dicha particion sin acceder a toda la tabla. 


