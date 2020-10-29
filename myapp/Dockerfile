# Pull base image.
FROM python:3.8.2

WORKDIR /app

# Copy artifacts
COPY proto/*.proto ./proto/
COPY src/* ./src/
COPY setup.py ./

# Build entry points
RUN python setup.py build_package_protos
RUN python setup.py develop

# Run the service
CMD ["grpc-server"]
