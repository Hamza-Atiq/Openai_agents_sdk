import os
import chainlit as cl
from dotenv import load_dotenv
from datetime import datetime
from typing import cast, List
from agents import Agent, Runner, function_tool, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set")

@cl.set_starters
async def set_starts() -> List[cl.Starter]:
    return [
        cl.Starter(
            label = "Greetings",
            message = "Hello! What can you help me with today?"
        ),
        cl.Starter(
            label = "Get Current Time",
            message = "What is the current time?"
        ),
        cl.Starter(
            label = "Get Current Date",
            message = "What is the current date?"
        ),
        cl.Starter(
            label = "Get Weather",
            message = "What is the weather in Karachi?"
        ),
        cl.Starter(
            label = "Find Student",
            message = "What is the name of the student with roll number 1?"
        ),
    ]
    
@function_tool("get_current_time")
@cl.step(type = "tool")
async def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@function_tool("get_current_date")
@cl.step(type = "tool")
async def get_current_date() -> str:
    return datetime.now().strftime("%Y-%m-%d")

@function_tool("get_weather")
@cl.step(type = "tool")
async def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny today."

@function_tool("piaic_student_finder")
@cl.step(type = "tool")
async def piaic_student_finder(student_roll_number: int) -> str:
    data = {
        1 : "Ali",
        2 : "Ahmad",
        3 : "Usman",
        4 : "Hassan",
        5 : "Hamza",
    }
    
    if student_roll_number in data:
        return f"The student with roll number {student_roll_number} is {data[student_roll_number]}."
    else:
        return f"No student found with roll number {student_roll_number}."
    
@cl.on_chat_start
async def start_chat():
    
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
    
    cl.user_session.set("history", [])
    
    cl.user_session.set("config", config)
    agent : Agent = Agent(
        name = "Assistant",
        instructions = "You are a helpful assistant that can answer questions and help with tasks.",
        model = model,
        tools = [get_current_time, get_current_date, get_weather, piaic_student_finder],
    )
    
    cl.user_session.set("agent", agent)
    
    await cl.Message(content = "Hi, I am the Assistant. How can I help you today?").send()
    
@cl.on_message
async def handle_message(message: cl.Message):
    
    msg = cl.Message(content = "Thinking...")
    await msg.send()
    
    config : RunConfig = cast(RunConfig, cl.user_session.get("config"))
    agent : Agent = cast(Agent, cl.user_session.get("agent"))
    
    history = cl.user_session.get("history", [])
    
    history.append({"role": "user", "content": message.content})
    
    try:
        
        print("\n[CALLING_AGENT_WITH_CONTEXT]\n", history, "\n")
        
        result = Runner.run_sync(
            starting_agent = agent,
            input = history,
            run_config = config,
        )
        
        response_content = result.final_output
        
        msg.content = response_content
        await msg.update()
        
        history.append({"role": "assistant", "content": response_content})
        cl.user_session.set("history", history)
        
        print(f"User: {message.content}\nAssistant: {response_content}\n")
    
    except Exception as e:
        print(f"Error: {e}")
        msg.content = "An error occurred while processing your request. Please try again later."
        await msg.update()