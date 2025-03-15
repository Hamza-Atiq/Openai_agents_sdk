import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled= True)

async def main():
    
    agent = Agent(
        name = "Assistant",
        instructions= "You only respond in haiku",
        model = OpenAIChatCompletionsModel(
            model = "gemini-1.5-flash",
            openai_client = external_client,
        ),
    )

    result = await Runner.run(
        agent,
        "Write me a haiku about a cat",     
    )
    
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())


