# Python Generators Project

This project demonstrates advanced usage of Python generators for memory-efficient data streaming, lazy loading, and aggregation from an SQL database.

## Project Structure
- `seed.py`: Sets up and seeds the MySQL database
- `0-stream_users.py`: Streams users one by one
- `1-batch_processing.py`: Processes users in batches
- `2-lazy_paginate.py`: Paginates users with lazy loading
- `4-stream_ages.py`: Streams user ages and computes average

## Requirements
- Python 3.x
- MySQL Server
- mysql-connector-python

## Usage
1. Run `seed.py` to setup and populate the database.
2. Execute scripts with corresponding `main.py` files to test functionalities.
