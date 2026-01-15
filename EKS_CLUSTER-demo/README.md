# DevOps-Cloud #
## Project Overview 
This project demonstrates a production-ready deployment of WordPress on Kubernetes using AWS EKS.  
The setup focuses on scalability, persistent storage, and clean separation between application and database layers.
---

## Problem Statement
Deploying WordPress in a production environment introduces multiple challenges:
- Ensuring data persistence for WordPress uploads and MySQL database
- Scaling the application easily under traffic
- Managing infrastructure efficiently
- Avoiding single points of failure

Traditional deployments on a single server make scaling, recovery, and maintenance difficult.

---

## Solution
This project solves these issues by deploying WordPress on Kubernetes (AWS EKS) with:
- **Amazon EFS** for shared WordPress storage (uploads)
- **Amazon EBS** for persistent MySQL database storage
- **Kubernetes LoadBalancer** service for external access
---

## Tech Stack
- AWS EKS
- Kubernetes
- Amazon EBS
- Amazon EFS
- WordPress
- MySQL
---
