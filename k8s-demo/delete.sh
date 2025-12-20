#!/bin/bash
#
kubectl delete svc app-svc
kubectl delete deploy deploy-1
kubectl delete sc demo-sc
kubectl delete pvc pvc-1
kubectl patch pvc pvc-1 -p '{"metadata":{"finalizers":null}}'
