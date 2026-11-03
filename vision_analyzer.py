"""
CAIO Workflow Vision Analyzer

Analyzes screenshots of business workflows using AI vision
to identify operational friction, workflow structure, and
potential automation opportunities.

Part of the AI Automation Consultant project.
"""

import base64
import os

from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
# Convert an image into a Base64-encoded string
def encode_image(image_path):
    """
    Read an image file and convert it to Base64.

    Args:
        image_path (str): Location of the image file.

    Returns:
        str: Base64-encoded image data.
    """
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(
            image_file.read()
        ).decode("utf-8")

    return encoded_image

def analyze_workflow_image(image_path):
    """
    Analyze a business workflow diagram using OpenAI Vision.

    Args:
        image_path (str): Path to the workflow image.

    Returns:
        str: AI-generated workflow analysis.
    """

    encoded_image = encode_image(image_path)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",

                    "text": (
                        "You are an AI Automation Consultant specializing in "
                        "business process improvement for small and mid-sized businesses. "
                        "Analyze the attached workflow diagram and provide a structured "
                        "automation assessment.\n\n"

                        "1. WORKFLOW OVERVIEW\n"
                        "Summarize the business process and its main steps.\n\n"

                        "2. MANUAL TASKS\n"
                        "Identify tasks that appear to require human effort. "
                        "Distinguish confirmed manual tasks from assumptions.\n\n"

                        "3. POTENTIAL BOTTLENECKS\n"
                        "Identify possible delays, repetitive activities, "
                        "handoffs, and operational inefficiencies.\n\n"

                        "4. AUTOMATION OPPORTUNITIES\n"
                        "Recommend up to three realistic automation opportunities. "
                        "For each, explain what could be automated and how.\n\n"

                        "5. EXPECTED BUSINESS BENEFITS\n"
                        "Describe potential time savings, improved consistency, "
                        "or reduced manual work. Do not invent numerical estimates.\n\n"

                        "6. DISCOVERY QUESTIONS\n"
                        "Ask up to three questions needed to validate the recommendations.\n\n"

                        "Use clear business language. "
                        "Do not invent details that are not visible in the diagram. "
                        "Clearly label assumptions and recommendations."
                    ),

                    },
                    {
                        "type": "input_image",
                        "image_url": (
                            f"data:image/png;base64,{encoded_image}"
                        ),
                    },
                ],
            }
        ],
    )

    return response.output_text

# Test the image encoding function
if __name__ == "__main__":
    image_path = "docs/images/sample_workflow.png"

    print("\nAI WORKFLOW VISION ANALYZER")
    print("=" * 45)

    print("\nAnalyzing workflow diagram...\n")

    analysis = analyze_workflow_image(image_path)

    print("WORKFLOW ANALYSIS")
    print("=" * 45)
    print(analysis)

    
# Test AI-powered workflow image analysis
if __name__ == "__main__":
    image_path = "docs/images/sample_workflow.png"
    report_path = "docs/reports/workflow_assessment.md"

    print("\nAI WORKFLOW VISION ANALYZER")
    print("=" * 45)

    print("\nAnalyzing workflow diagram...\n")

    analysis = analyze_workflow_image(image_path)

    print("WORKFLOW ANALYSIS")
    print("=" * 45)
    print(analysis)

    # Save the assessment for portfolio documentation
    with open(report_path, "w", encoding="utf-8") as report:
        report.write("# AI Workflow Automation Assessment\n\n")
        report.write("## Sample Workflow Analysis\n\n")
        report.write(analysis)

    print(f"\nAssessment saved to: {report_path}")
