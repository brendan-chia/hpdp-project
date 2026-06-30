# ============================================================================
# config.py — Central Configuration for the Kafka-Spark-Elasticsearch Pipeline
# ============================================================================
# This file holds all tuneable parameters for the streaming pipeline.
# Member 2 can adjust these settings without touching the main scripts.
# ============================================================================

import os

# ---------------------------------------------------------------------------
# Project Paths (relative to this config file's directory)
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)  # points to "hpdp project"

DATA_PATH = os.path.join(PROJECT_DIR, "data", "cleaned_data.csv")
MODEL_PATH = os.path.join(PROJECT_DIR, "models", "sentiment_model.pkl")
VECTORIZER_PATH = os.path.join(PROJECT_DIR, "models", "vectorizer.pkl")
LOG_DIR = os.path.join(BASE_DIR, "logs")

# ---------------------------------------------------------------------------
# Kafka Configuration
# ---------------------------------------------------------------------------
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC = "telecom-reviews"

# Delay (seconds) between each message sent by the producer.
# 0.05s ≈ 20 reviews/sec — adjust for faster/slower simulation.
PRODUCER_DELAY = 0.05

# ---------------------------------------------------------------------------
# Spark Configuration
# ---------------------------------------------------------------------------
SPARK_APP_NAME = "TelecomSentimentStreaming"

# ---------------------------------------------------------------------------
# Elasticsearch Configuration
# ---------------------------------------------------------------------------
ES_HOST = "localhost"
ES_PORT = "9200"
ES_INDEX = "telecom-sentiment"

# Full Elasticsearch nodes string for the ES-Hadoop connector
ES_NODES = f"{ES_HOST}:{ES_PORT}"
