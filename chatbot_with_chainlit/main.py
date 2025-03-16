import os 
import chainlit as cl
from dotenv import load_dotenv
from typing import cast
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set")

@cl.on_chat_start
async def start():
    
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
        tracing_disabled= True,
    )
    
    cl.user_session.set("chat_history", [])

    cl.user_session.set("config", config)
    
    agent: Agent = Agent(
        name = "Assistant",
        instructions = "You are a helpful assistant that can answer questions and help with tasks.",
        model = model,
    )
    
    cl.user_session.set("agent", agent)
    
    await cl.Message(content = "Hello! I'm the assistant. How can I help you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    
    msg = cl.Message(content = "Thinking...")
    await msg.send()
    
    agent:Agent = cast(Agent, cl.user_session.get("agent"))
    config: RunConfig = cast(RunConfig, cl.user_session.get("config"))
    
    history = cl.user_session.get("chat_history") or []
    
    history.append({"role": "user", "content": message.content})
    
    try:
        
        print("\n[CALLING_AGENT_WITH_CONTEXT]\n", history, "\n")
        result = Runner.run_sync(
            starting_agent=agent,
            input=history,
            run_config=config,
        )
        
        response_content = result.final_output
        
        msg.content = response_content
        await msg.update()
        
        history.append({"role": "assistant", "content": response_content})
        cl.user_session.set("chat_history", history)
        
        print(f"User: {message.content}\nAssistant: {response_content}\n")
        
    except Exception as e:
        print("\n[ERROR]\n", e, "\n")
        
        msg.content = "An error occurred while processing your request. Please try again later."
        
        await msg.update()
        
@cl.on_chat_end
async def on_chat_end():
    print("Chat ended")
    
    







