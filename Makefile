PIP: pip
NPM: npm
SLS: serverless
VERSION: v1

pipinit: requirements.txt
	$(PIP) install -r requirements.txt

npminit:
	$(NPM) install

init: pipinit npminit

local: init
	$(SLS) wsgi serve

dev-deploy: npminit
	$(SLS) deploy -s dev

product-deploy: npminit
	$(SLS) deploy -s $(VERSION)

clean: 
	rm -rf __pycache__