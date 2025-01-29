# GitEncryptor

GitEncryptor is a CLI tool written in Python that encrypts files before uploading them to a GitHub repository, ensuring data privacy both locally and in the cloud.

## ✨ Features

- 🔒 **AES-256 Encryption** – Protects your files before uploading.
- 🔍 **Integrity Verification** – Generates and validates SHA-256 hashes of stored files.
- 📂 **Secure Upload** – Supports single files, multiple files, and entire directories.
- 🔑 **On-Demand Decryption** – Downloads and decrypts files directly from GitHub.
- ⚡ **Simple CLI Interface** – Easy-to-use command-line parameters.

## 🚀 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/GitEncryptor.git
cd GitEncryptor
pip install -r requirements.txt
```

Or install directly via pip:

```bash
pip install git+https://github.com/your-username/GitEncryptor.git
```

## 🛠 Usage

### 1️⃣ Encrypt and upload a single file

```bash
python3 script66.py --encrypt_file /path/to/file.pdf --target_repo_url https://github.com/user/repository/ --time
```

### 2️⃣ Download and decrypt a single file

```bash
python3 script66.py --decrypt_url_file_repo https://github.com/user/repository/blob/main/file.pdf --dest_dir /destination/path --time
```

If the file has a specific hash:

```bash
python3 script66.py --decrypt_url_file_repo https://github.com/user/repository/blob/<hash>/file.pdf --dest_dir /destination/path --time
```

### 3️⃣ Encrypt and upload multiple files

```bash
python3 script66.py --encrypt_batch_file /path/file1.pdf /path/image.jpg /path/image.png --target_repo_url https://github.com/user/repository/ --time
```

### 4️⃣ Download and decrypt multiple files

```bash
python3 script66.py --decrypt_url_batch_file https://github.com/user/repository/blob/main/file1.pdf https://github.com/user/repository/blob/main/image.jpg https://github.com/user/repository/blob/main/image.png --dest_dir /destination/path --time
```

If the files have a specific hash:

```bash
python3 script66.py --decrypt_url_batch_file https://github.com/user/repository/blob/<hash>/file1.pdf https://github.com/user/repository/blob/<hash>/image.jpg https://github.com/user/repository/blob/<hash>/image.png --dest_dir /destination/path --time
```

### 5️⃣ Encrypt and upload an entire directory

```bash
python3 script66.py --encrypt_dir /path/to/directory/ --target_repo_url https://github.com/user/repository/ --time
```

### 6️⃣ Download and decrypt an entire repository

```bash
python3 script66.py --decrypt_url_repo https://github.com/user/repository/ --dest_dir /destination/path/ --time
```

## 📜 Command Line Options

| Argument                      | Description |
|--------------------------------|-------------|
| `--encrypt_file`              | Encrypts and uploads a single file to GitHub. |
| `--encrypt_batch_file`        | Encrypts and uploads multiple files to GitHub. |
| `--encrypt_dir`               | Encrypts and uploads an entire directory to GitHub. |
| `--target_repo_url`           | Specifies the destination GitHub repository URL. |
| `--decrypt_url_file_repo`     | Downloads and decrypts a single file from GitHub. |
| `--decrypt_url_batch_file`    | Downloads and decrypts multiple files from GitHub. |
| `--decrypt_url_repo`          | Downloads and decrypts an entire repository from GitHub. |
| `--dest_dir`                  | Defines the local directory for saving decrypted files. |
| `--time`                      | Measures execution time for operations. |

## 🎯 Complete Example

Encrypt and upload a file:

```bash
python3 script66.py --encrypt_file "/path/file.pdf" --target_repo_url "https://github.com/user/repository" --time
```

Download and decrypt a file from GitHub:

```bash
python3 script66.py --decrypt_url_file_repo "https://github.com/user/repository/blob/main/file.pdf" --dest_dir "/destination/path" --time
```

Download and decrypt an entire repository:

```bash
python3 script66.py --decrypt_url_repo "https://github.com/user/repository/" --dest_dir "/destination/path/" --time
```

## 🏗 Contributing

Feel free to open issues and pull requests!

📜 License: MIT
