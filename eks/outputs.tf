output "cluster_endpoint" {
    description = "The endpoint of the EKS cluster."
    value       = module.eks.cluster_endpoint

}

output "cluster_name" {
    description = "The name of the EKS cluster."
    value       = module.eks.cluster_name
}


output "vpc_id" {
  description = "The ID of the VPC where the EKS cluster is deployed."
  value       = module.vpc.vpc_id
}
