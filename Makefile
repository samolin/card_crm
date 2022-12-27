.PHONY: up
up:
	@docker-compose up --build -d

.PHONY: down
down:
	@docker-compose down

.PHONY: migrate
migrate:
	@docker exec crm_card python app/manage.py migrate --noinput

.PHONY: user
user:
	@docker exec crm_card python app/manage.py createsuperuser --email admin@admin.com --no-input