from daytona import Workflow, Artifact

workflow = Workflow()

@workflow.step
def register_code_image():
    """Register the Python code image as an artifact."""
    return Artifact(
        name="python_code_image",
        path="python_code_image.png",  # Local path in CodeSandbox
        type="image",
        external_url="https://your-storage-url/python_code_image.png"  # Optional: External URL if uploaded
    )

workflow.run()
