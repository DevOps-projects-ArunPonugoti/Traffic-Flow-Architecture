# Cloud-Native Application Traffic Flow Architecture


# From User Request to Container Response

A high-level visualization of how web traffic flows from a user's request through DNS resolution (Route53), GCP Load Balancer, Kubernetes Ingress Controller, Service, and finally to the application Pod - demonstrating the complete request-response cycle in a modern cloud-native infrastructure.


# Local vs Remote statefile
## Local
When you store your terrafrom statefile in the local system , at the same time multiple people wanna create mulitple resources it is very difcualt to give access to them , 

there is a chance tp create one resource multiple times , because everyone is using their own statefiles,

## Remote statefile
when you store statefile in the centralized location, multiple people can interact with it , they can create infra , and there is now chance for duplication
