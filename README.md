# XTS Cipher

A Python package for encryption and decryption using the XOR-Transposition-Substitution (XTS) cipher algorithm.

## Algorithm Overview: 

This algorithm combines Substitution, Transposition, and XOR operations to securely encrypt and decrypt a message.
1.	Substitution: Each character of the message is shifted by a key value (like a Caesar cipher).
2.	Transposition: The message is divided into blocks, and the order of these blocks is reversed.
3.	XOR: A series of keys are applied using the XOR operation to further obfuscate the message.

During decryption, the process is reversed:
1.	XOR: The XOR operation is applied using the same keys to reverse the encryption.
2.	Reverse Transposition: The blocks are rearranged back to their original order.
3.	Reverse Substitution: The characters are shifted back using the key to retrieve the original message.

## Features

- Generates random keys for encryption.
- Encrypts messages using substitution, transposition, and XOR operations.
- Decrypts messages back to the original form.

## Installation

You can install the package via pip:

```bash
pip install xts_cipher
