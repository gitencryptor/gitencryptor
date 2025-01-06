# GitEncryptor

GitEncryptor is a Python-based tool designed to securely manage and protect sensitive data within GitHub repositories, whether public or private. By combining best practices in cryptographic design and software engineering, GitEncryptor ensures data privacy and security, even in cloud environments where data custody may not be fully under the control of the data owner.

## Features

- **AES-256 Encryption**: Strong encryption using the AES-256 algorithm to secure sensitive files before uploading to GitHub.
- **File Integrity Check**: Automatically checks and verifies the integrity of files in the repository using MD5 hashes.
- **Modular Codebase**: A modular design that separates concerns into different classes, making the codebase maintainable and easy to extend.
- **Cloud-Friendly**: Provides data protection in cloud environments, ensuring that the owner’s data remains private.
- **Easy CLI Integration**: Supports command-line arguments for easy interaction, including options to encrypt/decrypt files.
  
## Requirements

- Python 3.x
