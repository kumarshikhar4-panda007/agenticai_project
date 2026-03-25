from azure.storage.blob import BlobServiceClient
from agent import summarize,extract_clauses,check_compliance
from PyPDF2 import PdfReader
import io

conn_str = "DefaultEndpointsProtocol=https;AccountName=legalstorage12;AccountKey=y2u7NFS04P0y7LkBhqrSnR/qGJKrK19+1XeqZzqx5loovrIZpwK94fDveLqkEVTi8LbnZfsPMQRI+AStsVwTXg==;EndpointSuffix=core.windows.net"

blob_service_client = BlobServiceClient.from_connection_string(conn_str)

container_name = "document-b10"

container_client = blob_service_client.get_container_client(container_name)

blob_name = "legal_document_B10.pdf"

blob_client = container_client.get_blob_client(blob_name)

content = blob_client.download_blob().readall()

reader = PdfReader(io.BytesIO(content))

text = ""
for page in reader.pages:
    extracted = page.extract_text()
    if extracted:
        text += extracted

clauses = extract_clauses(text)
compliance = check_compliance(text)
summary = summarize(text)


print("----SUMMARY----")
print(summary)
print("----CLAUSE----")
print(clauses)
print("----COMPLIANCE---")
print(compliance)