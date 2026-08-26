# Terraform volutamente insicuro: Checkov deve segnalare più issue.

resource "aws_s3_bucket" "logs" {
  bucket = "cerbercode-test-logs"
  # CKV_AWS_18: logging mancante
  # CKV_AWS_21: versioning mancante
  # CKV_AWS_145: encryption mancante
}

resource "aws_security_group" "open_ssh" {
  name = "open-ssh"

  # CKV_AWS_24: SSH aperto al mondo
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_instance" "app" {
  identifier        = "cerbercode-app-db"
  engine            = "postgres"
  instance_class    = "db.t3.micro"
  allocated_storage = 10
  username          = "admin"
  password          = "supersecret123!"  # CKV_SECRET_*: hardcoded password
  # CKV_AWS_16: encryption_at_rest mancante
  # CKV_AWS_17: backup_retention_period mancante
  skip_final_snapshot = true
}
