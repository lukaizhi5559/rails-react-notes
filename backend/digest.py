import bcrypt

# The hashed password
password_digest = b"$2a$12$z0i/dsdc9UeyQp9QoEz3UusDfr/QdOD8.l/xOawAsVcCMV5YQlSRi"

# The plain text password to check
candidate_password = b"test"

# Verify if the password matches the hash
if bcrypt.checkpw(candidate_password, password_digest):
    print("Password matches!")
else:
    print("Password does not match.")

