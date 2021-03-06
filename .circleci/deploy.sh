p#!/usr/bin/env bash

#set -o errexit
#set -o pipefail

download_terraform() {
    wget https://releases.hashicorp.com/terraform/0.11.4/terraform_0.11.4_linux_amd64.zip
    unzip terraform_0.11.4_linux_amd64.zip
    chmod +x terraform
    sudo mv terraform /usr/local/bin/
}

prepare_deployment_script() {
    cd ~
    git clone -b develop https://github.com/rnjane/finance-deployment-scripts.git
    cd ~/finance-deployment-scripts
    mkdir account-folder
    cd account-folder
    touch account.json

    echo ${SERVICE_ACCOUNT} > ~/finance-deployment-scripts/account-folder/account.json
}

check_branch(){
    REGION = ${REGION}
    PROJECT_ID = ${PROJECT_ID}
    CREDENTIALS = ${CREDENTIALS}
    ENVIRONMENT = ${ENVIRONMENT}
    IP_ADDRESS = ${IP_ADDRESS}
    MACHINE_TYPE = ${MACHINE_TYPE}
    NAME = ${NAME}
    ZONE = ${ZONE}
}

initialise_terraform() {
    cd ~/finance-deployment-scripts
    terraform init -lock=false -backend-config=bucket="${GCP_BUCKET}" -backend-config=prefix="/finance-terraform/${ENVIRONMENT}/finance.tfstate"
}

destroy_previous_infrastructure(){
    if [[ "$CIRCLE_BRANCH" == 'develop' || "$CIRCLE_BRANCH" == 'master' ]]; then
        terraform destroy -lock=false -auto-approve -var=project="${PROJECT_ID}" -var=ip-address="${IP_ADDRESS}" -var=env="${ENVIRONMENT}" -var=branch="${CIRCLE_BRANCH}" -var=host="${HOST}" -var=region="${REGION}" -var=zone="${ZONE}" -var=database_password="${DATABASE_PASSWORD}" -var=database_user="${DATABASE_USER}" -var=database_name="${DATABASE_NAME}" -var=postgres_ip="${POSTGRES_IP}" -var=environment="staging" -var=gs_bucket_name="${GS_BUCKET_NAME}" -var=gs_bucket_url="${GS_BUCKET_URL}" -var=cache_ip="${IP_ADDRESS}" -var=cache_port="${CACHE_PORT}"
    else
        terraform destroy -lock=false -auto-approve -var=project="${PROJECT_ID}" -var=ip-address="${IP_ADDRESS}" -var=env="${ENVIRONMENT}" -var=branch="${CIRCLE_BRANCH}" -var=host="${HOST}" -var=database_password="${DATABASE_PASSWORD}" -var=database_user="${DATABASE_USER}" -var=database_name="${DATABASE_NAME}" -var=postgres_ip="${POSTGRES_IP}" -var=environment="staging" -var=gs_bucket_name="${GS_BUCKET_NAME}" -var=gs_bucket_url="${GS_BUCKET_URL}" -var=cache_ip="${IP_ADDRESS}" -var=cache_port="${CACHE_PORT}"
    fi

}

#build_current_infrastructure() {
#    if [[ ! "$var1" =~ $re || "$CIRCLE_BRANCH" == 'develop' || "$CIRCLE_BRANCH" == 'master' ]]; then
#        terraform apply -lock=false -auto-approve -var=project="${PROJECT_ID}" -var=ip-address="${IP_ADDRESS}" -var=env="${ENVIRONMENT}" -var=branch="${CIRCLE_BRANCH}" -var=host="${HOST}" -var=region="${REGION}" -var=zone="${ZONE}" -var=database_password="${DATABASE_PASSWORD}" -var=database_user="${DATABASE_USER}" -var=database_name="${DATABASE_NAME}" -var=postgres_ip="${POSTGRES_IP}" -var=environment="staging" -var=gs_bucket_name="${GS_BUCKET_NAME}" -var=gs_bucket_url="${GS_BUCKET_URL}" -var=cache_ip="${IP_ADDRESS}" -var=cache_port="${CACHE_PORT}"
#    else
#        terraform apply -lock=false -auto-approve -var=project="${PROJECT_ID}" -var=ip-address="${IP_ADDRESS}" -var=env="${ENVIRONMENT}" -var=branch="${CIRCLE_BRANCH}" -var=host="${HOST}" -var=database_password="${DATABASE_PASSWORD}" -var=database_user="${DATABASE_USER}" -var=database_name="${DATABASE_NAME}" -var=postgres_ip="${POSTGRES_IP}" -var=environment="staging" -var=gs_bucket_name="${GS_BUCKET_NAME}" -var=gs_bucket_url="${GS_BUCKET_URL}" -var=cache_ip="${IP_ADDRESS}" -var=cache_port="${CACHE_PORT}"
#    fi
#}

main() {
    download_terraform
    prepare_deployment_script
    check_branch
    initialise_terraform
    destroy_previous_infrastructure
#    build_current_infrastructure
}

main "$@"