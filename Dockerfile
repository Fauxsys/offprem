# First Stage: Install dependencies, copy directory content, and build the package.
FROM python:latest AS builder
WORKDIR /offprem

RUN python -m pip install build

COPY . .

RUN python -m build --wheel

# Second Stage: Copy the built distribution from the first stage and install the package.
FROM python:3.9-slim
WORKDIR /code

COPY --from=builder /offprem/dist/ .

RUN python -m pip install *.whl

# Command to run on container start
# CMD [ "offprem" ]