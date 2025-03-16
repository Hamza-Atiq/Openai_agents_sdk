import os
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = external_client,
)

config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True,
)

@function_tool("get_current_time")
def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@function_tool("get_current_date")
def get_current_date() -> str:
    return datetime.now().strftime("%Y-%m-%d")

@function_tool("get_weather")
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny today."

@function_tool("piaic_student_finder")
def piaic_student_finder(student_roll_nummber : int) -> str:
    
    data = {
        1 : "Ali",
        2 : "Ahmad",
        3 : "Usman",
        4 : "Hassan",
        5 : "Hamza",
    }
    
    if student_roll_nummber in data:
        return f"The student with roll number {student_roll_nummber} is {data[student_roll_nummber]}."
    else:
        return f"No student found with roll number {student_roll_nummber}."
    
async def main():
    
    agent = Agent(
        name = "Assistant",
        instructions = "You are a helpful assistant that can answer questions and help with tasks.",
        model = model,
        tools = [get_current_time, get_current_date, get_weather, piaic_student_finder],
    )
    
    result_time = await Runner.run(
        starting_agent = agent,
        input = "What is the current time?",
        run_config = config,
    )
    
    print(result_time.final_output)
    
    result_date = await Runner.run(
        starting_agent = agent,
        input = "What is the current date?",
        run_config = config,
    )
    
    print(result_date.final_output)
    
    result_weather = await Runner.run(
        starting_agent = agent,
        input = "What is the weather in Karachi?",
        run_config = config,
    )
    
    print(result_weather.final_output)
    
    result_student = await Runner.run(
        starting_agent = agent,
        input = "What is the name of the student with roll number 1?",
        run_config = config,
    )
    
    print(result_student.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())
    