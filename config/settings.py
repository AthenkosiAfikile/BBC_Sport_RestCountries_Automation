import os


class Settings:
    pass


class Settings:
    pass
    BBC_SPORT_URL: str = "https://www.bbc.com/sport"
    BBC_SPORT_API_URL: str = "https://restcountries.com/v3.1"

    # Browser settings
    BROWSER: str = os.getenv("BROWSER", "chrome")
    HEADLESS_MODE: bool = os.getenv("HEADLESS_MODE", "True").lower() == "true"
    DEFAULT_WAIT_TIME: int = 15

    # Allure reporting
    ALLURE_RESULTS_DIR: str = "allure-results"
    ALLURE_REPORT_DIR: str = "allure-report"

    # Paths
    PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SCHEMAS_DIR: str = os.path.join(PROJECT_ROOT, "common", "schemas")

    settings = Settings()