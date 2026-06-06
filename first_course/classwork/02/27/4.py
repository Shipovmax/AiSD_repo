class CipherMaster:
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def process_text(self, text, shift, is_encrypt):
        text = text.lower()
        if not is_encrypt:
            shift = -shift

        result = []
        for char in text:
            if char in self.alphabet:
                index = self.alphabet.find(char)
                new_index = (index + shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                result.append(char)
        return "".join(result)


# Check
cipher_master = CipherMaster()
print(
    cipher_master.process_text(
        text="Once a reviewer accepted a project on the first try, and ever since then I have feared them",
        shift=2,
        is_encrypt=True,
    )
)
print(
    cipher_master.process_text(
        text="rqeg c tgxkgygt ceegrvgf c rtqlgev qp vjg hktuv vta, cpf gxgt ukpeg vjgp k jcxg hgctgf vjgo",
        shift=-3,
        is_encrypt=False,
    )
)
