variable "gcp_sa_key" {
  type = string
  description = "GCP SA Key used for deploy."
}

variable "image_name" {
  type = string
  description = "GCR image name."
  default = "aaml"
}

variable "target_project" {
  type = string
  description = "Project where the docker registry is located"
}

variable "service_version" {
  type = string
  description = "Service Version."
}

variable "secrets" {
    type = string
    description = "Docker secrets"
    default = ""
}

variable "build_args" {
    type = string
    description = "Docker build args"
    default = ""
}
