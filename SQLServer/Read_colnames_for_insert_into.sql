--Following code works on SQL Server and can be used to explicitly name columns in an insert statement in following syntax:
--Insert into db.schema.table (paste colnames here)

select stuff((
	select ',['+ column_name + ']'
	from db.information_schema.columns
	where table_name = 'tablename' and table_schema = 'schemaname'
	and ordinal_position > 1
	order by ordinal_position
	for xml path('')), 1, 1, ''
	)
