variable "bucket_name" {}

variable "provider" {
    type    = "map"
    default = {
        access_key = "unknown"
        secret_key = "unknown"
        region     = "unknown"
    }
}
