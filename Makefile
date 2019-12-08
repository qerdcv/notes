COMPOSE ?= docker-compose -f compose-base.yml

run: docker-build
	$(COMPOSE) up
	$(COMPOSE) down

docker-build:
	$(COMPOSE) build

remove-compose:
	$(COMPOSE) stop
	$(COMPOSE) rm -f
