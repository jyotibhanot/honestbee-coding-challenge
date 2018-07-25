### Terraform state

# This state creates s3 bucket for storing logs
- Commands:
  - terraform plan -var-file provider-credentials.tfvars -out s3bucket.tfplan
  - terraform apply s3bucket.tfplan 
  - terraform destroy -var-file provider-credentials.tfvars -force

- Files:
```
.
├── main.tf
├── provider-credentials.tfvars
├── README.md
├── s3bucket.tfplan
├── terraform.tfstate
├── terraform.tfstate.backup
└── variables.tf

0 directories, 7 files
```
