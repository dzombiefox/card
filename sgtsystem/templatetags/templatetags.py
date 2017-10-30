from django import template
register = template.Library()
@register.filter(name="encode_id")
def encoded_id(value):
        from Crypto.Cipher import AES
        import base64
        MASTER_KEY = "Some-long-base-key-to-use-as-encyrption-key"
        enc_secret = AES.new(MASTER_KEY[:32])
        tag_string = (str(value) +
                      (AES.block_size -
                       len(str(value)) % AES.block_size) * "\0")
        cipher_text = base64.b64encode(enc_secret.encrypt(tag_string))
        return cipher_text
