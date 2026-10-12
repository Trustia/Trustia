"""
Tests for Trustia Commercial Licensing & Cryptographic Verification Engine.
"""

import os
import tempfile
from core.licensing import LicenseManager


def test_create_and_verify_valid_license():
    lic = LicenseManager.create_license(
        client_name="Test Automotive Corp",
        expiry_date="2028-12-31",
        max_vehicles="50",
        tier="L4_ENTERPRISE_FULL_STACK"
    )
    assert lic["client_name"] == "Test Automotive Corp"
    assert "digital_signature" in lic
    
    is_valid, msg = LicenseManager.verify_license(lic)
    assert is_valid is True
    assert "GEÇERLİ" in msg


def test_tampered_license_fails():
    lic = LicenseManager.create_license(
        client_name="Legit Customer Ltd",
        expiry_date="LIFETIME"
    )
    
    # Tamper with the client name
    tampered = dict(lic)
    tampered["client_name"] = "Pirate Corp"
    
    is_valid, msg = LicenseManager.verify_license(tampered)
    assert is_valid is False
    assert "GEÇERSİZ LİSANS İMZASI" in msg


def test_save_and_load_license_file():
    lic = LicenseManager.create_license(
        client_name="Fleet Partner A.S.",
        expiry_date="LIFETIME",
        max_vehicles="UNLIMITED"
    )
    
    with tempfile.TemporaryDirectory() as tmpdir:
        lic_path = os.path.join(tmpdir, "trustia.lic")
        saved_path = LicenseManager.save_license_file(lic, lic_path)
        assert os.path.exists(saved_path)
        
        loaded_data, is_valid, msg = LicenseManager.load_license_file(lic_path)
        assert is_valid is True
        assert loaded_data["client_name"] == "Fleet Partner A.S."


def test_system_status_evaluation_fallback():
    # In non-existing file scenario, it should fallback to evaluation mode safely
    status = LicenseManager.get_system_status("non_existent_file.lic")
    assert status["mode"] == "EVALUATION_DEMO"
    assert status["is_authorized"] is True
