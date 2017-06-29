--Following code works on SQL Server and can be used to explicitly name columns in an insert statement in following syntax:
--Insert into db.schema.table (paste colnames here)
--where-clause with ordinal_position zorgt ervoor dat je bepaalde kolommen kunt uitslutien (bijv een eerste kolom met identity)

select stuff((
	select ',['+ column_name + ']'
	from db.information_schema.columns
	where table_name = 'tablename' and table_schema = 'schemaname'
	and ordinal_position > 0
	order by ordinal_position
	for xml path('')), 1, 1, ''
	)
