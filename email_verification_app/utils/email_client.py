from typing import Optional, List

import requests
from dotenv import load_dotenv
import os

load_dotenv()


class EmailVerificationClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.hunter.io/v2/"

    @staticmethod
    def generate_param(value: List[str]) -> str:
        return ",".join(value) if value else ""

    def domain_search(
        self,
        domain: str,
        email_type: Optional[List[str]],
        seniority: Optional[List[str]],
        department: Optional[List[str]],
        required_field: Optional[List[str]],
        company: Optional[str],
        limit: Optional[int] = 10,
        offset: Optional[int] = 0,
    ) -> dict:
        params = {
            "domain": domain,
            "company": company,
            "api_key": self.api_key,
            "limit": limit,
            "offset": offset,
            "type": self.generate_param(email_type),
            "seniority": self.generate_param(seniority),
            "department": self.generate_param(department),
            "required_field": self.generate_param(required_field),
        }
        response = requests.get(f"{self.base_url}domain-search", params=params)
        return response.json()

    def email_finder(
        self,
        domain: str,
        first_name: str,
        last_name: str,
        company: Optional[str] = "",
        full_name: Optional[str] = "",
        max_duration: Optional[int] = 10,
    ) -> dict:
        params = {
            "domain": domain,
            "first_name": first_name,
            "last_name": last_name,
            "company": company,
            "full_name": full_name,
            "api_key": self.api_key,
            "max_duration": max_duration,
        }
        response = requests.get(f"{self.base_url}email-finder", params=params)
        return response.json()

    def email_verifier(self, email: str) -> dict:
        params = {
            "email": email,
            "api_key": self.api_key,
        }
        response = requests.get(f"{self.base_url}email-verifier", params=params)
        return response.json()

    def email_count(
        self, domain: str, email_type: Optional[List[str]], company: Optional[str] = ""
    ) -> dict:
        params = {
            "domain": domain,
            "company": company,
            "type": self.generate_param(email_type),
            "api_key": self.api_key,
        }
        response = requests.get(f"{self.base_url}email-verifier", params=params)
        return response.json()

    def account(self) -> dict:
        params = {
            "api_key": self.api_key,
        }
        response = requests.get(f"{self.base_url}account", params=params)
        return response.json()


verification_client = EmailVerificationClient(api_key=os.getenv("API_KEY"))
