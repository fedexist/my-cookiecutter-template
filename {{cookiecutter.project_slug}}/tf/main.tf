terraform {
  required_version = "~> 1.0.0"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "~> 3.88.0"
    }
  }
  backend "gcs" {
    prefix = "{{ cookiecutter.tenant_name }}/{{ cookiecutter.project_slug }}"
  }
}

locals {
  # Labels to be attached to each resource
  legal_entity = "{{ cookiecutter.legal_entity.lower() }}"
  business_unit = "{{ cookiecutter.business_unit }}"
  tenant_name = "{{ cookiecutter.tenant_name }}"
  project_slug = "{{ cookiecutter.project_slug }}"
  labels = {
    le = local.legal_entity
    bu = local.business_unit
    tenant = local.tenant_name
    project_slug = local.project_slug
  }
}

#
# Build Docker Image
#
module "{{ cookiecutter.project_slug }}_docker_image" {
    source = "gcs::https://storage.googleapis.com/storage/v1/generali-it-nonprod-mlt-advana-000013-eu-tf-modules-nnjnz/docker-build/tf-1.0.9-v1.0/module.zip"
    dockerfile_folder = "${abspath(path.module)}/../"
    gcr_image_name = var.gcr_image_name
    gcp_sa_key = var.gcp_sa_key
    gcr_target_project = var.gcr_target_project
    docker_build_args = var.docker_build_args
    gcr_image_tags = var.image_tags
}
