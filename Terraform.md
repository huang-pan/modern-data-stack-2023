# Terraform

## Terraform

- Terraform, Vault, and Packer https://www.youtube.com/watch?v=tckVYA9_Wwg
	- Vault: store secrets
	- Packer: package up virtual machine images
- ****Terraform + dbt Cloud, Fivetran, etc****
	- https://youtube.com/watch?v=vkQsGLhqF6I&si=1oOeiFz-m5yneqTf
	- https://www.youtube.com/watch?v=OHzZ7KuioMA
	- https://www.youtube.com/watch?v=SPcwo0Gq9T8
- Refresher lecture, just the basics
	- [https://www.youtube.com/watch?v=7xngnjfIlK4](https://www.youtube.com/watch?v=7xngnjfIlK4)
 	- terraform init
 	- terraform plan: show the plan to create / update the infrastructure
  		- terraform config: what you want the infrastructure to be
    		- terraform state: what the infrastructure actually is
  ![terraform state](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e866dfd4-cc46-490e-95da-3cdb0578b536)

  	- terraform apply: apply the plan
  	- terraform destroy
  	- IaC
		- variables, for loops, count, depends on, providers
		- perform actions on local or remote (terraform registry)
	- modules https://www.youtube.com/watch?v=fg67eIMmB_U
		- package and reuse resource configurations, collection of .tf files
			- compute.tf
			- database.tf
			- dns.tf
			- main.tf 
			- variables.tf 
			- ...
		- root module: all ..tf files in the main working directory
		- child modules
			- parameterized using different input variables
	- registry.terraform.io: contains many common modules
	- multiple environments (dev / stg / prod)
		- workspaces (not recommended)
		- file structure: recommended, separate directories for dev / stg / prod with .tf, .tfvars files in each directory
		- possible multiple AWS accounts, one for each environment (dev / stg / prod)
	- testing
		- static checks: terraform fmt, validate, plan
		- external: tflint
	- workflow
		- run code changes locally -> PR -> CI tests -> PR merge to main CD (staging) -> main merge to release CD (prod)
	- terragrunt / gruntwork.io; clean terraform code DRY, multiple cloud accounts
- YAML: how YAML is structured
 	- https://www.linkedin.com/posts/eniolaamiola_devops-kubernetes-k8s-activity-7124334714789711872-8Zv8/
  	- scalars, lists, nested lists, dictionaries, nested dicts, comments
- Terraform best practices
	- https://www.youtube.com/watch?v=gxPykhPxRW0
