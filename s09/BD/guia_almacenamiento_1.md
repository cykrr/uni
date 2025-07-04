# Gestión de almacenamiento

## Objetivos
1. Comprender cómo Oracle organiza los datos a través de tablespaces, datafiles
y bloques de datos.
2. Conocer las configuraciones de tablespaces y cómo verificar su uso y
configuración en Oracle 21c.
3. Prácticas de administración para crear, modificar y gestionar tablespaces.

## Conceptos: Estructura y almacenamiento de datos en oracle

Tablespace: Contenedor lógico de almacenamiento que organiza el espacio donde se
alojan los datos. Estos se componen de archivos físicos en el disco llamados
datafiles.

Cada Tablespace está respaldado por uno o varios datafile que contienen
físicamente los datos. Estos suelen estar ubicados en $ORACLE_HOME/oradata/xe.
Los nombres suelen tener una extensión .dbf por ejemplo `system01.dbf` o 
`sysaux01.dbf`.

Oracle permite ver los tablespaces en la base de datos mediante las vistas del
diccionario de datos. La consulta principal para listar los tablespaces es:

```
SQL> select TABLESPACE_NAME,STATUS,CONTENTS,SEGMENT_SPACE_MANAGEMENT from DBA_TABLESPACES;

TABLESPACE_NAME                STATUS    CONTENTS              SEGMEN
------------------------------ --------- --------------------- ------
SYSTEM                         ONLINE    PERMANENT             MANUAL
SYSAUX                         ONLINE    PERMANENT             AUTO
UNDOTBS1                       ONLINE    UNDO                  MANUAL
TEMP                           ONLINE    TEMPORARY             MANUAL
USERS                          ONLINE    PERMANENT             AUTO
HR_TABLESPACE                  ONLINE    PERMANENT             AUTO
```
`TABLESPACE_NAME`: Nombre del tablespace
`STATUS`: Estado del Tablespace, (Online o Offline)
`CONTENTS`: Define si el tablespace es de tipo datos, temporal o de UNDO.
`SEGMENT_SPACE_MANAGEMENT`: Muestra si se gestiona automáticamente (AUTO) o manualmente (MANUAL).

Para ver los datafiles asociados a cada tablespace:
```
select FILE_NAME, TABLESPACE_NAME, BYTES, STATUS from DBA_DATA_FILES;
FILE_NAME
--------------------------------------------------------------------------------
TABLESPACE_NAME                     BYTES STATUS
------------------------------ ---------- ---------
C:\APP\KRR\PRODUCT\21C\ORADATA\XE\USERS01.DBF
USERS                             5242880 AVAILABLE

C:\APP\KRR\PRODUCT\21C\ORADATA\XE\UNDOTBS01.DBF
--------------------------------------------------------------------------------
TABLESPACE_NAME                     BYTES STATUS
------------------------------ ---------- ---------
C:\APP\KRR\PRODUCT\21C\ORADATA\XE\USERS01.DBF
USERS                             5242880 AVAILABLE

C:\APP\KRR\PRODUCT\21C\ORADATA\XE\UNDOTBS01.DBF
UNDOTBS1                        120586240 AVAILABLE

C:\APP\KRR\PRODUCT\21C\ORADATA\XE\SYSTEM01.DBF
SYSTEM                         1426063360 AVAILABLE


FILE_NAME
--------------------------------------------------------------------------------
TABLESPACE_NAME                     BYTES STATUS
------------------------------ ---------- ---------
C:\APP\KRR\PRODUCT\21C\ORADATA\XE\SYSAUX01.DBF
SYSAUX                          891289600 AVAILABLE

C:\APP\KRR\PRODUCT\21C\ORADATA\XE\HR_TABLESPACE.DBF
HR_TABLESPACE                   104857600 AVAILABLE
```
## Tipo de Tablespaces 
`SYSTEM` y `SYSAUX`: Tablespaces obligatorios para la base de datos que
contienen datos de sistema, metadatos y diccionarios.

`TEMP`: Tablespace temporal que Oracle usa para operaciones temporales (como
ordenamientos y joins complejos).

`UNDO`: Tablespace usado para almacenar información de deshacer (rollback) de
transacciones.

Tablespaces de usuario: Espacio dedicado a almacenar datos de usuario o 
aplicaciones. E.g.: Users.

## Creación de un Tablespace
Crear un tablespace permite organizar mejor los datos. Se puede especificar un
tamaño inicial y, si es necesario, permitir que el tablespace crezca
automáticamente.

### Ejemplo de creación de un tablespace 'DATA_TBS' de 50MB en la ubicación predeterminada

```
CREATE TABLESPACE DATA_TBS 
DATAFILE 'C:\APP\KRR\PRODUCT\21C\ORADATA\XE\DATA_TBS01.dbf'
SIZE 50M
AUTOEXTEND ON
NEXT 10M MAXSIZE 500M;
```

`DATAFILE`: Ruta y nombre del archivo físico. 
`SIZE`: Tamaño inicial del archivo. 
`AUTOEXTEND`: Permite que el archivo crezca automáticamente. 
`NEXT`: Tamaño en MB para cada aumento automático. 
`MAXSIZE`: Tamaño máximo que el archivo puede alcanzar. 

## Modificación de un Tablespace

Si se necesita ampliar el tamaño de un tablespace manualmente, se puede utilizar

```
ALTER DATABASE DATAFILE 'C:\APP\KRR\21C\ORADATA\XE\DATA_TBS01.dbf' RESIZE 100M;
```
Este comando redimensiona el datafile `data_tbs01.dbf` a 100MB.

## Consulta del espacio disponible

```
SELECT TABLESPACE_NAME,  
        ROUND(SUM(BYTES) / (1024 * 1024), 2) AS TOTAL_MB, 
        ROUND(SUM(FREE_SPACE) / (1024 * 1024), 2) AS FREE_MB 
 FROM DBA_FREE_SPACE  
 GROUP BY TABLESPACE_NAME; 
```

`TOTAL_MB`: Espacio total asignado al tablespace. 
`FREE_MB`: Espacio libre disponible. 
