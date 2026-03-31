"""Module for handling Two-Factor Authentication."""
import pyotp

class Auth2FA:
    """Generates and verifies TOTP codes."""

    def __init__(self):
        # In production, store this uniquely per user in a database
        self.secret = pyotp.random_base32()

    def get_provisioning_uri(self, user_email):
        """Returns a URI to generate a QR code for Authenticator apps."""
        return pyotp.totp.TOTP(self.secret).provisioning_uri(
            name=user_email, 
            issuer_name="CryPTrus 2.0"
        )

    def verify_code(self, code):
        """Verifies the 6-digit code provided by the user."""
        totp = pyotp.totp.TOTP(self.secret)
        return totp.verify(code)

    def current_otp(self):
        """Returns the current valid code (for testing)."""
        return pyotp.totp.TOTP(self.secret).now()
