from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]

llm = ChatGroq(model="llama-3.3-70b-versatile")
# response = llm.invoke("What is the meaning of life?")
# print(response)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
           "system", # information for LLM
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools.
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("human", "{query}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

chain = prompt | llm | parser

query = input("What can I help you research ? \nEnter your query : ")
response = chain.invoke({"query":query})

print(response)

try:
    print(response.topic)
    print(response.summary)
    print(response.sources)
except Exception as e:
    print("Error Parsing Response",e)


