terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.17.0"
    }
  }
}

provider "google" {
  project = "de-zoomcamp-448210"
  region  = "australia-southeast1-a"
}

resource "google_storage_bucket" "test-bucket" {
  name          = "de-zoomcamp-448210-bucket"
  location      = "AUSTRALIA-SOUTHEAST1"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}