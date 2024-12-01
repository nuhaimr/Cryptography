# Cryptography Assignments - README

## Overview

This repository contains two assignments focused on cryptographic algorithms and their implementation in Python. These assignments cover concepts like frequency analysis, brute-force attacks, DES encryption/decryption, and RSA encryption. Each assignment includes Python scripts, test files, and documentation.

---

## Repository Structure

### Assignment 1

This assignment explores classical cryptography techniques, including frequency analysis and affine cipher attacks, as well as DES encryption.

- **Files:**
  - `Q1a.py`: Implements letter frequency analysis to decrypt text.
  - `Q1b.py`: Performs a brute-force attack on the affine cipher.
  - `Q2.py`: Implements DES (Data Encryption Standard) for encryption and decryption.
  - `DES-test.txt`: Test file containing data for DES encryption.
  - `cipher.txt`: Stores encrypted or decrypted outputs.

---

### Assignment 2

This assignment focuses on RSA (Rivest–Shamir–Adleman) encryption and decryption.

- **Files:**
  - `RSA.py`: Implements RSA encryption, decryption, and key generation.
  - `RSA-test.txt`: Test input file for verifying the RSA implementation.
  - `20696366_Report.pdf`: Detailed report explaining the RSA algorithm and its implementation.

---

## Getting Started

### Prerequisites

- Python 3.x installed.
- Basic understanding of cryptographic algorithms such as DES, RSA, and affine ciphers.

---

## Assignment 1 Instructions

### **Q1a.py: Letter Frequency Analysis**

1. **Purpose:**
   - Decrypt text based on frequency analysis of letters.

2. **Execution:**
   ```bash
   python Q1a.py <file_path>
   ```
   Replace `<file_path>` with the path to the encrypted text file.

3. **Example:**
   ```bash
   python Q1a.py DES-test.txt
   ```

---

### **Q1b.py: Affine Cipher Brute-Force Attack**

1. **Purpose:**
   - Brute-force attack on an affine cipher.

2. **Execution:**
   ```bash
   python Q1b.py <file_path>
   ```
   Replace `<file_path>` with the path to the encrypted affine cipher text.

---

### **Q2.py: DES Encryption/Decryption**

1. **Purpose:**
   - Encrypt and decrypt data using the DES algorithm.

2. **Execution:**
   ```bash
   python Q2.py
   ```

3. **Input:**
   - Use `DES-test.txt` for testing DES operations.

---

## Assignment 2 Instructions

### **RSA.py: RSA Encryption and Decryption**

1. **Purpose:**
   - Implements RSA encryption, decryption, and key generation.

2. **Execution:**
   ```bash
   python RSA.py
   ```

3. **Test File:**
   - `RSA-test.txt` contains test cases for verifying RSA operations.

4. **Output:**
   - Encrypted and decrypted results are stored in `cipher.txt`.

---

## Outputs

- **`cipher.txt`**: Stores results of encryption/decryption operations.
- **Test files**:
  - `DES-test.txt`: Input for DES encryption/decryption.
  - `RSA-test.txt`: Input for RSA implementation testing.

---

## Notes

- Ensure that the input files are formatted correctly for each script.
- Modify paths in the scripts if running in a different environment.
- Refer to `20696366_Report.pdf` for a detailed explanation of the RSA implementation.

---

## Contact

For any issues or queries, please refer to the project report or contact the maintainer.

---

*Explore the fascinating world of cryptography!* 🔒
