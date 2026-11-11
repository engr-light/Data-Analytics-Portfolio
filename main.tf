resource "aws_s3_bucket" "soc_telemetry" {
  bucket = "soc-telemetry-archive-el" # Ensure your initials are here
}

resource "aws_s3_bucket_versioning" "soc_telemetry_versioning" {
  bucket = aws_s3_bucket.soc_telemetry.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_athena_database" "security_telemetry" {
  name   = "security_telemetry_db"
  bucket = aws_s3_bucket.soc_telemetry.id
}