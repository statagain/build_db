CREATE_DATASET_DDL = """
CREATE TABLE IF NOT EXISTS dataset(
  id VARCHAR(20) PRIMARY KEY,
  short_name VARCHAR(40),
  name VARCHAR(250) NOT NULL,
  url VARCHAR(2048),
  attribution TEXT,
  desc TEXT
);
"""

CREATE_FEATURE_DDL = """
CREATE TABLE IF NOT EXISTS feature(
  dataset_id VARCHAR(20),
  name varchar(250) NOT NULL,
  desc TEXT,
  FOREIGN KEY(dataset_id) REFERENCES dataset(id)
);
"""
