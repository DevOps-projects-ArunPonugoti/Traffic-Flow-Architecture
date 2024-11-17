from diagrams import Diagram, Edge, Cluster
from diagrams.gcp.storage import Storage
from diagrams.onprem.client import Users
from diagrams.generic.blank import Blank

with Diagram("Terraform State Locking Process", show=True, direction="TB"):
    # Users
    user1 = Users("Developer 1")
    user2 = Users("Developer 2")
    user3 = Users("Developer 3")

    # GCP Storage for Remote State
    gcs_bucket = Storage("Remote State\n(GCS Bucket)")
    lock = Storage("State Lock File")

    # Workflow
    user1 >> Edge(color="green", label="Request Lock (terraform apply)") >> lock
    lock >> Edge(color="blue", label="Lock Active") >> gcs_bucket

    user2 >> Edge(color="red", style="dashed", label="Wait for Lock") >> lock
    user3 >> Edge(color="red", style="dashed", label="Wait for Lock") >> lock

    # Unlocking
    gcs_bucket >> Edge(color="green", label="Unlock State (terraform done)") >> lock
