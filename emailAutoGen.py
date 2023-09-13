import os
from dotenv import load_dotenv

from pydantic import BaseModel
import asyncio

from langchain import PromptTemplate
from langchain.agents import initialize_agent, load_tools
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.llms import OpenAI
from langchain.utilities.zapier import ZapierNLAWrapper
from langchain.utilities import SerpAPIWrapper


# GET KEY FROM .env
load_dotenv()
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")


# Data 
class Data(BaseModel):
    yourname: str
    phone: str
    email: str
    customer: str
    product: str
    details: str
    result: str

async def loadPrompt():
    file_path = 'prompt.txt'

    # Initialize an empty str
    data = ''

    # Open the file in read mode and read its content line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Add each line to the end (stripped of leading/trailing whitespace) to the 'data'
            data += line.strip() + '\n'

    return data

async def generateEmail(data: Data):
    # Create prompt
    prompt = await loadPrompt()

    # Set up OpenAI
    openai = OpenAI(
        model_name="text-davinci-003",
        openai_api_key=OPENAI_API_KEY
    )

    # Set up prompt config
    promptConfig = PromptTemplate(
        input_variables=['yourname', 'phone', 'email', 'customer', 'product', 'details'],
        template=prompt
    )

    # Get result
    result = openai(
        promptConfig.format(
            yourname = data.yourname,
            phone = data.phone,
            email = data.email,
            customer = data.customer,
            product = data.product,
            details = data.details
        )
    )
    await asyncio.sleep(3)
    return result



