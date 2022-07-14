CREATE_DATASET_DDL = """
CREATE TABLE IF NOT EXISTS dataset(
  id VARCHAR(20) PRIMARY KEY,
  name VARCHAR(40),
  title VARCHAR(250) NOT NULL,
  url VARCHAR(2048),
  attribution TEXT,
  description TEXT
);
"""

CREATE_FEATURE_DDL = """
CREATE TABLE IF NOT EXISTS feature(
  dataset_id VARCHAR(20),
  name VARCHAR(250) NOT NULL,
  description TEXT,
  FOREIGN KEY(dataset_id) REFERENCES dataset(id)
);
"""
