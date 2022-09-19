terraform {
  required_version = "~> 1.0.0"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "~> 3.88.0"
    }
  }
  backend "gcs" {
    prefix = "ml-ops/{{ cookiecutter.project_slug }}"
  }
}

module "{{ cookiecutter.package_name }}_docker_image" {
     source = "./platform-terraform-modules/docker-build/tf-1.0.9-v2.0"
     dockerfile = "${abspath(path.module)}/../Dockerfile"
     build_folder = "${abspath(path.module)}/../"
     gcp_sa_key = var.gcp_sa_key
     target_project = var.target_project
     image_name = var.image_name
     image_tags = [
       var.service_version,
       "latest"
    ]
    docker_secrets = var.secrets
    docker_build_args = var.build_args
}
