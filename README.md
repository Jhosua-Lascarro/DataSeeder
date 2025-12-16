# DataSeeder

Synthetic data generation and seeding tool for Supabase databases.

## Description

DataSeeder is a Python tool that generates and loads synthetic data into Supabase databases. It uses Faker for realistic data generation, Pandera for schema validation, and provides a complete pipeline that respects entity relationships.

## Table of Contents

- [Features](#features)
- [Supported Entities](#supported-entities)
- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
- [Author](#author)

## Features

- Automated pipeline with sequential data generation respecting table dependencies
- Schema validation using Pandera to ensure data integrity
- Realistic synthetic data generation with Faker
- Support for creating users in Supabase auth.users
- Dry-run mode to test the pipeline without inserting real data
- Modern dependency management using UV

## Supported Entities

The system generates data for the following entities:

1. **Auth Users** - Supabase authentication users
2. **Clients** - Clients with roles and status
3. **Products** - Product catalog with inventory
4. **Sales** - Sales linked to products and users
5. **Activity Logs** - System activity records

## Installation

### Prerequisites

- Python 3.14+
- UV (Python package manager)
- Supabase account with service credentials

### Installation Steps

1. **Clone the repository**:
```bash
git clone <repository-url>
cd DataSeeder
```

2. **Install dependencies**:
```bash
make sync
# Or directly: uv sync
```

3. **Configure environment variables**:

Create a `.env` file in the project root:

```env
URL=https://your-project.supabase.co
SERVICE_ROLE_KEY=your-service-role-key
DRY_RUN=false
```

## Usage

### Run the Complete Pipeline

```bash
make pipeline
# Or directly: uv run src/dataseeder/pipeline.py
```

### Available Make Commands

```bash
make help         # Show help
make sync         # Install dependencies
make install      # Install package in editable mode with pip
make pipeline     # Run the generation pipeline
make test         # Run tests
make format       # Format code with Ruff
make clean        # Clean Python temporary files
make docker-build # Build Docker image
make docker-run   # Run Docker container
```

### Dry Run Mode

To test the pipeline without inserting real data:

```env
DRY_RUN=true
```

## Docker

### Build the Docker Image

```bash
make docker-build
# Or directly: docker build -t dataseeder:latest .
```

### Run with Docker

```bash
make docker-run
# Or directly: docker run --env-file .env -it dataseeder:latest
```

The Dockerfile uses the official UV Python image and includes:
- Python 3.14 base image
- Production dependencies only (no dev packages)
- Automatic pipeline execution on container start

### Environment Variables for Docker

Make sure your `.env` file contains the required Supabase credentials before running the container.

## Author

**Jhosua Lascarro**
- GitHub: [@Jhosua-Lascarro](https://github.com/Jhosua-Lascarro)