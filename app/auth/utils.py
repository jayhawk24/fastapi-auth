import bcrypt


def hash_pass(password: str):
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)

    return hashed_password.decode("utf-8")


def verify_password(non_hashed_pass, hashed_pass):
    password_byte_enc = non_hashed_pass.encode("utf-8")
    hashed_pass = hashed_pass.encode("utf-8")

    return bcrypt.checkpw(password=password_byte_enc, hashed_password=hashed_pass)
