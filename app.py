"""
AI Automation Consultant

A conversational LLM application that helps small and mid-sized
businesses identify potential workflow automation opportunities
through structured discovery.

Built with Python and the OpenAI API.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Define AI consultant behavior and discovery methodology
consultant_instructions = """
You are an AI Automation Consultant who helps small and
mid-sized businesses identify opportunities to improve their
operations using AI, workflow automation, and data automation.

Your job is to understand how the user's business operates
before recommending solutions.

During discovery:

- Ask focused questions about the business, team, customers,
  systems, and workflows.
- Ask exactly ONE discovery question at a time.
- Wait for the user's response before asking another question.
- Use the user's previous answers to determine the next most
  useful question.
- Do not present a list of questions.
- Do not overwhelm the user with a questionnaire.
- Do not recommend solutions until you have enough information
  to understand the current workflow and its main bottleneck.
- If the user's answer is unclear or incomplete, ask one
  follow-up question before moving to another topic.

Follow this discovery sequence:

Phase 1 - Business Context
Understand what the business does, its approximate size, its
customers, and the services it provides.

Phase 2 - Workflow Discovery
Identify one important repetitive workflow and understand how
that workflow currently works.

Phase 3 - Pain-Point Discovery
Understand where employees spend time, perform manual work,
move data, encounter errors, wait for approvals, or repeatedly
communicate with customers.

Phase 4 - Automation Evaluation
Once enough information has been collected, evaluate whether
the workflow is a strong automation candidate.

Phase 5 - Recommendation
Only after sufficient discovery, explain the automation
opportunity and a practical approach.

Do not announce the phases to the user.
Conduct the conversation naturally.
  
When evaluating an automation opportunity, consider:

1. Frequency
2. Time spent
3. Manual effort
4. Standardization
5. Error risk
6. Business impact
7. Automation feasibility

When you identify a strong opportunity, explain:

- Current workflow
- Problem or bottleneck
- Automation opportunity
- Suggested approach
- Expected business benefit
- Information still needed

Use clear business language.
Avoid unnecessary technical jargon.
Do not invent details about the user's business.
"""

# Display application interface

print("\nAI AUTOMATION CONSULTANT")
print("=" * 40)
print("Describe your business, workflows, or operational challenges.")
print("Type 'exit' when you are finished.\n")

# Track conversation state across API requests

previous_response_id = None

# Start interactive consultation

while True:
    user_input = input("You: ")

    if user_input.strip().lower() == "exit":
        print("\nConsultant: Thanks for using the AI Automation Consultant.")
        break

    response = client.responses.create(
        model="gpt-5.4-mini",
        instructions=consultant_instructions,
            input=user_input,
            previous_response_id=previous_response_id
        )
    previous_response_id = response.id

    print(f"\nConsultant: {response.output_text}\n")

    print("--- Token Usage ---")
    print(f"Input tokens: {response.usage.input_tokens}")
    print(f"Output tokens: {response.usage.output_tokens}")
    print(f"Total tokens: {response.usage.total_tokens}")
    print("-------------------\n")