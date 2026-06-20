from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv('client_id')

print(client_id)