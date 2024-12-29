"""
Fonction Python qui décrypte le message en effectuant un décalage inverse de 7 lettres.
"""
def decrypt_message(message):
    
    decrypted_message = ""
    
    for char in message:
        if char.isalpha():
            # Gérer le décalage en tenant compte des majuscules et minuscules
            offset = 65 if char.isupper() else 97
            decrypted_message += chr((ord(char) - offset - 7) % 26 + offset)
        else:
            # Si ce n'est pas une lettre, ajoute-le tel quel
            decrypted_message += char
    
    return decrypted_message

# Message à décrypter
encrypted_message = "mlspjpahapvuz, jlzhy zlyhpa mply kl avp, zp zlbsltlua ps jvuuhpzzhpa wfaovu"

# Décryptage du message
print("Message décrypté :", decrypt_message(encrypted_message))


######################################### Sortie ###################################################

""" 
Message décrypté : felicitations, cesar serait fier de toi, si seulement il connaissait python
"""

####################################################################################################