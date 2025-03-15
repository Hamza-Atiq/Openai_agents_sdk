import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-1.5-flash",
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

agent : Agent = Agent(
    model=model,
    name = "Assistant",
    instructions = "You are a helpful assistant that can answer questions and help with tasks.",
)

result = Runner.run_sync(
    agent,
    "Assalamo Alikum, how are you? I am a new user of this platform. I am trying to learn about the OpenAI agents SDK and how to use it.",
    run_config = config,
)

print(result.final_output)