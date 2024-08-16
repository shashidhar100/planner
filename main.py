from langchain.memory import ConversationBufferMemory
import chainlit
from langchain.schema.messages import AIMessage
from CustomAgent import createCustomAgent
from Model import getOpenAIChatModel
from CustomTool import getPackages


data = AIMessage(content="Hello")
data.to_json()
data.content[0]

model = getOpenAIChatModel(temperature=0,streaming=True)
tools = [getPackages]


@chainlit.on_chat_start
async def OnChatStart():
    print("OnChatStart")
    memory = ConversationBufferMemory(memory_key="chat_history",input_key="input", output_key="output",return_messages=True)
    agentChain = createCustomAgent(tools=tools,llm=model,memory=memory)
    
    chainlit.user_session.set("agentChain", agentChain)
    await chainlit.Message(content="Hello! I'm a travel agent. I can help you find the perfect vacation package based on your preferences. Please provide me with the location, budget, and duration of your trip.").send()

@chainlit.on_message
async def OnMessage(message: chainlit.Message):
    
    agentChain = chainlit.user_session.get("agentChain")    
    cb = chainlit.AsyncLangchainCallbackHandler()
    res = await agentChain.arun(message.content,callbacks=[cb]) 
    await chainlit.Message(content=res).send()