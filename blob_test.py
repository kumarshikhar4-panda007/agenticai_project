from azure.storage.blob import BlobServiceClient

conn_str = "DefaultEndpointsProtocol=https;AccountName=legalstorage12;AccountKey=y2u7NFS04P0y7LkBhqrSnR/qGJKrK19+1XeqZzqx5loovrIZpwK94fDveLqkEVTi8LbnZfsPMQRI+AStsVwTXg==;EndpointSuffix=core.windows.net"

blob_service_client = BlobServiceClient.from_connection_string(conn_str)

container_name = "document-b10"

blobs = blob_service_client.get_container_client(container_name).list_blobs()

for blob in blobs:
    print(blob.name)