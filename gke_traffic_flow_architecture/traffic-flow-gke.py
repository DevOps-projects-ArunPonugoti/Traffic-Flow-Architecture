from diagrams import Diagram, Edge
from diagrams.onprem.client import Users
from diagrams.aws.network import Route53
from diagrams.gcp.network import LoadBalancing
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.compute import Pod

# Create the traffic flow diagram
with Diagram(
    name="Traffic Flow: User to Container",
    filename="traffic_flow",  # Specify filename
    show=True,  # Change to True to display
    direction="TB",
    outformat="png"  # Explicitly specify output format
):
    # Use Users instead of Datacenter since Datacenter isn't available
    user = Users("Customer")
    
    # DNS (Domain Name System)
    dns = Route53("DNS")
    
    # GCP Load Balancer
    lb = LoadBalancing("GCP Load Balancer")
    
    # Kubernetes Components
    ingress = Ingress("Ingress Controller")
    service = Service("Kubernetes Service")
    pod = Pod("Application Pod")
    
    # Define traffic flow
    user >> Edge(label="1. Request: www.example.com") >> dns
    dns >> Edge(label="2. Resolves to IP") >> lb
    lb >> Edge(label="3. Routes to Ingress") >> ingress
    ingress >> Edge(label="4. Routes to Service") >> service
    service >> Edge(label="5. Routes to Pod") >> pod
    pod >> Edge(label="6. Sends Response") >> service
    service >> Edge(label="7. Back to Ingress") >> ingress
    ingress >> Edge(label="8. Back to Load Balancer") >> lb
    lb >> Edge(label="9. Response to Customer") >> user