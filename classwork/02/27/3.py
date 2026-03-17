class CipherMaster:
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def cipher(self, original_text, shift):
        original_text = original_text.lower()
        result = []

        for char in original_text:
            if char in self.alphabet:
                index = self.alphabet.find(char)
                new_index = (index + shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                result.append(char)

        return "".join(result)

    def decipher(self, cipher_text, shift):
        return self.cipher(cipher_text, -shift)


# Usage example
cipher_master = CipherMaster()

print(
    cipher_master.cipher(
        original_text="Once a reviewer accepted a project on the first try, and ever since then I have feared them",
        shift=2,
    )
)

print(
    cipher_master.decipher(
        cipher_text="rqeg c tgxkgygt ceegrvgf c rtqlgev qp vjg hktuv vta, cpf gxgt ukpeg vjgp k jcxg hgctgf vjgo",
        shift=-3,
    )
)
