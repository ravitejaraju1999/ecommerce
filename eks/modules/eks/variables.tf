variable "cluster_name" {
  description = "The name of the EKS cluster."
  type        = string
}

variable "cluster_version" {
  description = "The Kubernetes version for the EKS cluster."
  type        = string
  default     = "1.24"
}

variable "vpc_id" {
  description = "The ID of the VPC where the EKS cluster will be deployed."
  type        = string
}

variable "subnet_ids" {
  description = "A list of IDs for the private subnets."
  type        = list(string)
}

variable "node_groups" {
  description = "eks node group configurations."
  type = map(object({
    name           = string
    instance_types  = list(string)
    capacity_type   = string
    scaling_config = object({
      desired_size   = number
      max_size       = number
      min_size       = number
    })
  }))
}