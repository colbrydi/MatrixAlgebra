init:
	conda env create --file environment.yml --name MTH314
    
.PHONY: init docs lint test 
