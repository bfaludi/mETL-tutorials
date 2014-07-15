diff source/current.json source/new.json
metl -t migration.pickle -s source/current.json 01_migration.yml
metl -m migration.pickle -t new_migration.pickle -s source/new.json 01_migration.yml 
metl-differences new_migration.pickle migration.pickle

# New:		1
# Updated:	1
# Unchanged:	237
# Deleted:	1

metl-differences -d 02_deleted.yml new_migration.pickle migration.pickle