import json
import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib
import argparse
from github import Github

class CryptographyUtil:
    @staticmethod
    def encrypt(raw, key, is_text=True):
        iv = get_random_bytes(16)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv) if is_text else AES.new(key.encode('utf-8'), AES.MODE_ECB)
        encrypted = cipher.encrypt(pad(raw.encode() if is_text else raw, 32))
        return base64.b64encode(iv + encrypted)

    @staticmethod
    def decrypt(enc, key, is_text=True):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv) if is_text else AES.new(key.encode('utf-8'), AES.MODE_ECB)
        decrypted = unpad(cipher.decrypt(enc[16:]), 32)
        return decrypted

class GitHubUtil:
    @staticmethod
    def file_exists_in_repo(repo, file_path):
        try:
            repo.get_contents(file_path)
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_file_content(file_path, key):
        with open(file_path, 'rb') as file:
            binary_content = file.read()
            encrypted_content = CryptographyUtil.encrypt(binary_content, key, is_text=False)
            return encrypted_content.decode('utf-8')

    @staticmethod
    def add_file(repo, file_path, content, key):
        commit_message = f'Add {file_path} via Python script'
        try:
            repo.create_file(file_path, commit_message, content)
            print(f'Arquivo {file_path} enviado com sucesso para o GitHub!')
            return True
        except Exception as e:
            print(f'Erro ao adicionar arquivo {file_path}. Código de status: {e}')
            return False

    @staticmethod
    def update_file(repo, file_path, content, key):
        commit_message = f'Update {file_path} via Python script'
        try:
            current_content = CryptographyUtil.decrypt(repo.get_contents(file_path).content, key, is_text=False)
            if content != current_content:
                repo.update_file(file_path, commit_message, content, current_content)
                print(f'Arquivo {file_path} atualizado com sucesso no GitHub!')
                return True
            else:
                print(f'Arquivo {file_path} já existe no GitHub e não precisa ser atualizado.')
                return False
        except Exception as e:
            print(f'Erro ao atualizar arquivo {file_path}. Código de status: {e}')
            return False

class FileUtil:
    @staticmethod
    def upload_file_to_github(repo, file_path, key):
        content = GitHubUtil.get_file_content(file_path, key)
        relative_path = os.path.basename(file_path)

        if GitHubUtil.file_exists_in_repo(repo, relative_path):
            GitHubUtil.update_file(repo, relative_path, content, key)
        else:
            GitHubUtil.add_file(repo, relative_path, content, key)

    @staticmethod
    def upload_directory_to_github(repo, directory_path, key):
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            if os.path.isfile(file_path):
                # Ajuste do caminho para ser relativo ao repositório
                relative_path = os.path.basename(file_path)

                if not GitHubUtil.file_exists_in_repo(repo, relative_path):
                    FileUtil.upload_file_to_github(repo, file_path, key)

    @staticmethod
    def calculate_local_md5(file_path, key):
        with open(file_path, 'rb') as f:
            md5_hash = hashlib.md5()
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)
        return CryptographyUtil.encrypt(md5_hash.hexdigest(), key).decode('utf-8')

    @staticmethod
    def check_file_md5(file_path, repo, key):
        envelop = json.dumps({"cypher_version": "1", "action_version": "1", "name": file_path})
        request_result = json.loads(repo.post("info_file.php", envelop))

        local_md5 = FileUtil.calculate_local_md5(file_path, key)

        print(f"  \033[94m\033[1mLocal MD5\033[0m {local_md5}")
        print(f"  \033[94m\033[1mServer MD5\033[0m {request_result['info']['md5']}")

        if local_md5 == request_result['info']['md5']:
            print("\033[92m\033[1mIgual\033[0m", file_path)
            return True
        else:
            print("\033[91m\033[1mDiferente\033[0m", file_path)
            return False

    @staticmethod
    def decrypt_file(encrypted_file_path, key):
        with open(encrypted_file_path, 'rb') as file:
            encrypted_content = file.read()
            decrypted_content = CryptographyUtil.decrypt(encrypted_content, key, is_text=False)
            decrypted_file_path = f'decrypt_{os.path.basename(encrypted_file_path)}'
            with open(decrypted_file_path, 'wb') as decrypted_file:
                decrypted_file.write(decrypted_content)
            print(f'Arquivo descriptografado: {decrypted_file_path}')

def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config

def main():
    parser = argparse.ArgumentParser(description='Script de Upload e Download Seguro para o GitHub.')
    parser.add_argument('-d', '--decrypt', help='Descriptografa o arquivo. Informe o caminho do arquivo criptografado.', metavar='encrypted_file_path')
    args = parser.parse_args()

    config = load_config()
    key = input('Digite a chave de criptografia para AES-256 (32 caracteres): ')
    key = key[:32].rjust(32, '-')

    g = Github(config['token'])
    repo = g.get_user(config['username']).get_repo(config['repo_name'])
    directory_path = config['directory_path']

    if args.decrypt:
        FileUtil.decrypt_file(args.decrypt, key)
    else:
        FileUtil.upload_directory_to_github(repo, directory_path, key)

if __name__ == '__main__':
    main()