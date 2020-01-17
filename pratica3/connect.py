from cassandra.cluster import Cluster

def connect(keyspace, address='127.0.0.1', port=9042):
    cluster = Cluster([address], port=port)
    session = cluster.connect(keyspace, wait_for_all_pools=True)
    session.execute(f'USE {keyspace}')

    return session
