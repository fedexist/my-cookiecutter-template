// Auto-Generated Variables
env.ENV = "dev"

env.STATE_BUCKET = "generali-it-nonprod-mlt-advana-000012-tfstate"
env.TERRAFORM_SA_CRED_NAME = "terraform-${env.LE}-${env.ENV}-json"

env.PYPI_REGISTRY = "europe-west3-python.pkg.dev"
env.DOCKER_REGISTRY = "europe-west3-docker.pkg.dev"
env.ARTIFACT_PROJECT = "it-nonprod-gen-advana-000007"
env.PYPI_REPO = "https://${PYPI_REGISTRY}/it-prod-gen-advana-000040/pypi/"
env.DOCKER_URL = "${DOCKER_REGISTRY}/${ARTIFACT_PROJECT}/docker-images"
env.BASE_IMAGE = "${DOCKER_URL}/aa-python:3.9-slim"

// User-Defined Variables
env.TARGET_PROJECT_ID = "it-nonprod-gen-advana-000007"
