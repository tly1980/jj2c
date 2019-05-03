```yaml
tables:
  users:
    - field: name
      type: string
    - field: age
      type: int
    - field: state
      type: string
      partitioned_by: true
```


With following template code

```jinja2
{{ load_table_definition | tables.json }}

{{ spark_table_schema_def | 'users', 'gs://a/b/c', 'abc_schema' }}
```

translated into

```sql
-- load_table_definition:
--   users{name(string), age(int), state(string, partitioned_by)}

CREATE TABLE IF NOT EXISTS `abc`.`user`
(
  `name` STRING,
  `age` INT,
  `state` STRING
)
USING PARQUET
OPTIONS (
  path 'gs://a/b/c'
)
PARTITIONED BY `state`;

```

