import random
import httpx
from datetime import datetime
from pydantic_settings import BaseSettings


class GitHubController:
    def __init__(self, base_url: str, repo_name: str, api_token: str):
        self.base_url = base_url
        self.repo_name = repo_name
        self.api_token = api_token
    
    
    async def _commit_new_data_to_main_(self, data: dict[str,str]):
        url = f"{self.base_url}/repos/{self.repo_name}/contents/data.json"
        print(url)
        return


class Config(BaseSettings):
    github_base_url: str = "https://api.github.com"
    github_repo_name: str = "your-repo-name"
    github_api_token: str = "your-github-api-token"
    
    class ConfigDict:
        env_file = ".env"


async def main():
    try:
        config = Config()
        date = datetime.now().strftime("%Y-%m-%d")
        random_ten_digit_string = ''.join(random.choices('0123456789', k=10))
        final_payload = {
            "date": date,
            "random_string": random_ten_digit_string
        }
        gitHub_client = GitHubController(base_url=config.github_base_url,
                                         repo_name=config.github_repo_name,
                                         api_token=config.github_api_token)
        result = gitHub_client._commit_new_data_to_main_(data=final_payload)
        print(f"Data committed successfully: {result}")
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        print(f"Request error occurred: {e}")
    except KeyError as e:
        print(f"Key error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e



import asyncio

if __name__ == "__main__":
    asyncio.run(main())
    print("Script executed successfully.")