import os
import subprocess
from Utilities.common_methods import instantPrint, removeSpecialCharactersAndSpaces, createFolderIfNotExists
import json
from Utilities.enums import AccessibilityType

class GitHubSupport:
    def __init__(self) -> None:
        self.initialize_parameters()
        self.handler = GitHubHandler()
        
    def initialize_parameters(self):
            """
            Initializes the parameters for the GitHub assistant.

            Reads the repository data from the 'github_data.json' file and sets the
            'repos', 'office_repo_dir', and 'personal_repo_dir' attributes of the class.

            Parameters:
                None

            Returns:
                None
            """
            repo_data = json.load(open("ApplicationData/github_data.json"))
            self.repos = repo_data["repos"]
            self.office_repo_dir = repo_data["local office repo folder"]
            self.personal_repo_dir = repo_data["local personal repo folder"]
            self.visual_studio_path = repo_data["visual studio 2022 path"]

    def clone_repo(self, repo_name) -> bool:
        """
        Clones a repository with the given name.

        Args:
            repo_name (str): The name of the repository to clone.

        Returns:
            bool: True if the repository was successfully cloned, False otherwise.
        """
        repo_name = removeSpecialCharactersAndSpaces(repo_name)
        matched_repo = [repo for repo in self.repos if repo["name"]==repo_name]
        if len(matched_repo)==0:
            instantPrint(f"Repository {repo_name} not found")
            return False
        local_repo_path = self.office_repo_dir if matched_repo[0]["accessibility"]== AccessibilityType.OFFICE.value else self.personal_repo_dir
        local_repo_path += matched_repo[0]["path"]
        self.handler.clone_repo(matched_repo[0]["remote"], local_repo_path=local_repo_path)
        return True

    def pull_latest_changes_for_current_branch(self, repo_name):
        pass

class GitHubHandler:
    def __init__(self) -> None:
        pass

    def clone_repo(self, remote_path, local_repo_path=None):
        """
        Clones a repository from the specified `repo_path` into the local repository.

        Args:
            repo_path (str): The URL or path of the repository to clone.

        Returns:
            None
        """
        createFolderIfNotExists(local_repo_path)
        print(f"Cloning {remote_path} in {local_repo_path}")
        os.system(f'git clone {remote_path} {local_repo_path}')

    def pull_latest_changes(self):
        pass

    
    import os

    # Path to your Visual Studio installation
    vs_path = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"

    # Path to your .NET solution file
    solution_path = "C:\\path\\to\\your\\solution.sln"

    # Check if the paths exist
    if os.path.exists(vs_path) and os.path.exists(solution_path):
        # Open the solution in Visual Studio
        subprocess.Popen([vs_path, solution_path])
    else:
        print("Visual Studio or the solution file does not exist at the provided paths.")


if __name__=="__main__":
    githubSupport = GitHubSupport()
    githubSupport.clone_repo("pricesheet")
    
