# Auto-Generated Variables
variable "gcp_sa_key" {
  type = string
  description = "GCP SA Key used for deploy."
}

variable "gcr_image_name" {
  type = string
  description = "GCR image name."
}

variable "gcr_target_project" {
  type = string
  description = "GCR Target project where the image is pushed."
}

# Used-Defined Variables

variable "build_args" {
  type = string
  description = "Docker build args (KEY1=VALUE1,KEY2=VALUE2)."
  default = ""
}

variable "image_tags" {
  type = list(string)
  description = "This is the tag which will be used for the image that you created to push"
  default = [
    "latest"
  ]
}
