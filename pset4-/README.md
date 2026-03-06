# PSet 4 – Encryption and Decryption (One-Time Pad)

## Overview
This project implements a simple encryption and decryption system using a **one-time pad** technique.

The program can:
- Encrypt plaintext messages
- Decrypt ciphertext using a known pad
- Attempt to find the correct pad from a list of possible pads

The correct pad is determined by selecting the one that produces the **largest number of valid English words** when decrypting the ciphertext.

---

## Features

### PlaintextMessage
Represents a message before encryption.

Responsibilities:
- Store the original plaintext
- Store the pad used for encryption
- Generate the encrypted message using the pad

---

### EncryptedMessage
Represents an encrypted message.

Responsibilities:
- Store the ciphertext
- Decrypt the message using a given pad
- Attempt decryption with multiple pads

The program evaluates each decrypted result and chooses the pad that produces the **highest number of valid English words**.

If multiple pads produce the same maximum number of valid words, the **last pad** is selected.

---

## Key Functions

### `decrypt_message_try_pads(ciphertext, pads)`

Attempts to decrypt a ciphertext using a list of possible pads.

**Parameters**

- `ciphertext` – an `EncryptedMessage` object  
- `pads` – a list of pads (each pad is a list of integers)

**Process**

1. Decrypt the ciphertext using each candidate pad
2. Count valid English words in the resulting plaintext
3. Select the pad producing the highest score

**Returns**

A `PlaintextMessage` object containing:
- the decrypted message
- the pad used

---

### `decode_story()`

Decodes Bob's encrypted story using the provided pads.

Steps:
1. Load the encrypted story
2. Load the list of possible pads
3. Try decrypting with each pad
4. Return the most likely plaintext

Example:

```python
print(decode_story())