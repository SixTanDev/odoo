#!/bin/bash

# Install project dependencies using Poetry
poetry install

exec "$@"