init:
	conda env create --prefix ./envs --file environment.yml
    
.PHONY: init docs lint test 
