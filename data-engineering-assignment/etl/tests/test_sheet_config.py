"""
Smoke test for Google Sheets configuration.
"""

from etl.config.sheet_config import load_sheet_config, SheetConfigError


def test_sheet_config():
    try:
        config = load_sheet_config()

        assert config.sheet_id
        assert config.range_name
        assert config.service_account_file

        print("✅ Sheet configuration test PASSED")

    except SheetConfigError as e:
        print("❌ Sheet configuration test FAILED")
        raise e


if __name__ == "__main__":
    test_sheet_config()
