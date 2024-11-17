from diagrams import Diagram, Edge, Cluster
from diagrams.gcp.storage import Storage
from diagrams.gcp.compute import ComputeEngine
from diagrams.onprem.client import Users
from diagrams.generic.storage import Storage as LocalStorage
from diagrams.generic.blank import Blank

with Diagram("Local vs Remote State Management", show=True, direction="TB"):
    # Local State Management
    with Cluster("Local State Management"):
        admin1_local = Users("Admin 1 (Local)")
        admin2_local = Users("Admin 2 (Local)")
        admin3_local = Users("Admin 3 (Local)")

        local_tf_state = LocalStorage("Local State File")
        vm_local = ComputeEngine("VM Instance (Conflict Risk)")

        # Local connections
        admin1_local >> Edge(color="red", label="Access Local State") >> local_tf_state
        admin2_local >> Edge(color="red", label="Access Conflict!") >> local_tf_state
        admin3_local >> Edge(color="red", label="Access Conflict!") >> local_tf_state
        local_tf_state >> Edge(color="red", label="Race Condition Risk") >> vm_local

    # Remote State Management
    with Cluster("Remote State Management"):
        admin1_remote = Users("Admin 1 (Remote)")
        admin2_remote = Users("Admin 2 (Remote)")
        admin3_remote = Users("Admin 3 (Remote)")

        remote_tf_state = Storage("Remote State (GCS Bucket)")
        state_lock = Storage("State Lock File")
        vm_remote = ComputeEngine("VM Instance (No Conflict)")

        # Remote connections
        admin1_remote >> Edge(color="green", label="Access Remote State") >> remote_tf_state
        admin2_remote >> Edge(color="green", label="Wait for Lock") >> remote_tf_state
        admin3_remote >> Edge(color="green", label="Wait for Lock") >> remote_tf_state

        # Locking mechanism
        remote_tf_state >> Edge(color="blue", label="State Lock") >> state_lock
        remote_tf_state >> Edge(color="green", label="Apply Changes") >> vm_remote
