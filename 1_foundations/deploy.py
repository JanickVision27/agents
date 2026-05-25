from huggingface_hub import HfApi

REPO_ID = "JanickVision/career_conversations"

api = HfApi()

print(f"🚀 Uploading to {REPO_ID} ...")

api.upload_folder(
    folder_path=".",
    repo_id=REPO_ID,
    repo_type="space",
    commit_message="Update career_conversations app",
    ignore_patterns=[
        "__pycache__/**",
        "**/__pycache__/**",
        ".gradio/**",
        "*.pyc",
        ".env",
        ".env.*",
        ".venv/**",
        "venv/**",
        "deploy.py",
        ".git/**",
        ".gitignore",
        ".ipynb_checkpoints/**",
        "**/.ipynb_checkpoints/**",
    ],
)

print("✅ Upload complete!")
print(f"   https://huggingface.co/spaces/{REPO_ID}")
