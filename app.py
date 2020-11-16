import os
import re
import paramiko
from dotenv import load_dotenv

# SSH infos
load_dotenv()
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
USER = os.getenv('USER')
KEY_PATH = os.getenv('KEY_PATH')

# mv file dir
IMAGE_DIR = os.getenv('IMAGE_DIR')
REMOTE_IMAGE_DIR = os.getenv('REMOTE_IMAGE_DIR')

# image regex
IMG_REGEX = r'^\d{4}-\d{4}-\d{6}_+[a-zA-Z0-9_]*.(jpg|jpeg|png|ping)$'

# SSH
with paramiko.SSHClient() as ssh:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(HOST, PORT, USER, key_filename=KEY_PATH)
    
    # sftp put
    with client.open_sftp() as sftp:
        img_paths = [img for img in os.listdir(IMAGE_DIR) if re.search(IMG_REGEX, img)]
        for img_path in img_paths:
            sftp.put(, REMOTE_IMAGE_DIR)
