build_image:
	sudo docker build -t odoo .

build:
	sudo docker-compose build

run_odoo:
	sudo docker-compose up -d

interactive_odoo:
	docker exec -u 0 -it odoo-container /bin/bash

interactive_development:
	docker exec -u 0 -it development_python /bin/bash

create_module:
	docker exec -u 0 -it odoo-container odoo scaffold checklist_management /mnt/extra-addons

pre_commit:
	pre-commit run --all-files

[.PHONY]: run_odoo interactive_odoo create_module interactive_development build build_image
