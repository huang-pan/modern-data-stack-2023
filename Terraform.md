# Terraform
![mail](https://github.com/user-attachments/assets/0dec92e5-876f-4a34-a75f-6b300c96e7c8)

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
- https://www.atlassian.com/incident-management/kpis/sla-vs-slo-vs-sli
	- SLA: Service Level Agreement, the agreement you make with your clients or users
 	- SLO: Service Level Objectives, the objectives your team must hit to meet that agreement
	- SLI: Service Level Indicators, the real numbers on your performance
- Terraform Variables Tutorial: Mastering Input and Output Variables https://www.youtube.com/watch?v=5COJ40HE_q8
![Screenshot_20240630-170811_YouTube](https://github.com/user-attachments/assets/81821291-b613-4233-9bd1-9a40352d7826)
![Screenshot_20240630-170932_YouTube](https://github.com/user-attachments/assets/35467453-d979-4fb6-87b2-aa978c46c0e0)
- https://www.linkedin.com/posts/govardhana-miriyala-kannaiah_many-devops-engineers-dont-fully-understand-activity-7319193025266556930-u8Zt/
![1744948443804](https://github.com/user-attachments/assets/c2295e42-af42-473e-85ad-bcad5147c7af)
