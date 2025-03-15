import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_default_openai_client, set_tracing_disabled

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)
set_tracing_disabled(disabled= True)

model = OpenAIChatCompletionsModel(
    model = "gemini-1.5-flash",
    openai_client = external_client,
)

agent : Agent = Agent(
    name = "Assistant",
    instructions = "You are a helpful assistant that can answer questions and help with tasks.",
    model = model,

)

result = Runner.run_sync(
    agent,
    "Hello, how are you?",
)

print(result.final_output)
