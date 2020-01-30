SELECT
  COUNT(*)
FROM
  information_schema.tables
WHERE
  table_schema = 'mediawiki';
