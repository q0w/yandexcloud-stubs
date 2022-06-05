.PHONY: clone deps proto

clone:
	git clone --recurse-submodules https://github.com/yandex-cloud/python-sdk.git sdk

deps:
	python -m pip install --upgrade pip
	python -m pip install grpcio-tools mypy-protobuf

proto:
	python3 -m grpc_tools.protoc \
	--proto_path=sdk/cloudapi \
	--proto_path=sdk/cloudapi/third_party/googleapis \
	--mypy_out=. \
	--mypy_grpc_out=. \
	`find sdk/cloudapi/yandex -name '*.proto'`
	find yandex -type d -exec touch {}/__init__.pyi \;