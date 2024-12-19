# Kubernetes

## Kubernetes tutorial
- https://blog.bytebytego.com/p/kubernetes-when-and-how-to-apply
- Refresher lecture, just the basics
	- [https://www.youtube.com/watch?v=X48VuDVv0do](https://www.youtube.com/watch?v=X48VuDVv0do)
- https://youtu.be/s_o8dwzRlu4
	- more concise summary of k8s architecture
	- State full sets hard to manage, easier to use db services outside k8s
- https://www.linkedin.com/posts/nasiullha-chaudhari_kubernetes-interview-qa-activity-7193482366181396481-S5Fu/
	- ****great detailed explanation of k8s****
- Volumes, volume mounts, persistent volume claim
	- https://www.kubermatic.com/blog/keeping-the-state-of-apps-1-introduction-to-volume-and-volumemounts/
	- https://bluexp.netapp.com/blog/cvo-blg-kubernetes-persistent-volume-claims-explained
- stateful set
	- https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
 	- Like a Deployment, a StatefulSet manages Pods that are based on an identical container spec. Unlike a Deployment, a StatefulSet maintains a sticky identity for each of its Pods. These pods are created from the same spec, but are not interchangeable: each has a persistent identifier that it maintains across any rescheduling. 
![k8s](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f932b21f-e33f-45d3-811a-0df5e3d610bb)
![k8s design patterns](https://github.com/user-attachments/assets/c5683ab0-7eba-41d0-b409-1527898b9805)
![sidecar](https://github.com/user-attachments/assets/5d50f8b0-3aa2-423e-b48b-cf59e362cdc0)


- ****Tilt**** for K8s https://www.youtube.com/watch?v=JRc967vAkGM
	- tool for making k8s dev easier
 	- simplify Kubernetes development with Tilt, a tool that enables hot reloading, automatic code syncing, and centralized log monitoring across microservices
