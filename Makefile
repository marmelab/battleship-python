DOCKER := docker run -it --rm battleship-python

install: ## Build the docker container
	docker build -t battleship-python .

run: ## Run the game.
	$(DOCKER) python3 ./main.py player1=player1