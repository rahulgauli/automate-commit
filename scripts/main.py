import json
import random
import httpx
from datetime import datetime
from pydantic_settings import BaseSettings

from github import Auth
from github import Github


class GitHubController:
    def __init__(self, repo_name: str, api_token: str):
        self.repo_name = repo_name
        self.api_token = api_token
        

    async def _get_github_client(self):
        try:
            auth = Auth.Token(self.api_token)
            github_client = Github(auth=auth)
            return github_client
        except Exception as e:
            print(f"Error creating GitHub client: {e}")
            raise e
    

    async def _get_repo_(self, github_client: Github):
        try:
            print(f"logged in you are huhuhuwahhah: {github_client.get_user().login}")
            repo = github_client.get_repo(self.repo_name)
            print(f"Connected to repository: {repo.name}")
            return repo
        except Exception as e:
            print(f"Error getting repository: {e}")
            raise e

    async def _commit_new_data_to_main_(self, data: dict[str,str]):

        github_client = await self._get_github_client()
        repo = await self._get_repo_(github_client)
        try:
            random_16_digit_string = ''.join(random.choices('0123456789', k=16))
            file_name = f"data_{random_16_digit_string}.json"
            file_content = json.dumps(data, indent=4)
            create_a_new_file = repo.create_file(
                path=file_name,
                message=f"Add new data file: {file_name}",
                content=file_content,
                branch="main"
            )
            print(f"File created successfully: {create_a_new_file}")
            return True
        except Exception as e:
            print(f"Error committing new data: {e}")
            raise e


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
        gitHub_client = GitHubController(
                                         repo_name=config.github_repo_name,
                                         api_token=config.github_api_token
                                         )
        result = await gitHub_client._commit_new_data_to_main_(data=final_payload)
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