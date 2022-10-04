
local:
	docker-compose -f docker-compose-local.yml up -d

backend:
	mkdir -p odoo_data
	chmod -R 777 odoo_data
	docker-compose up -d

db:
	docker-compose -f docker-compose-db.yml up -d

push:
	git add . && git commit -m "update" && git push github master

pull:
	git pull github master && docker restart sn
