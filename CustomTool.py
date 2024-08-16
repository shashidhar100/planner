
import json
from typing import Any, Coroutine, Optional, Type
from langchain.tools import StructuredTool,BaseTool,tool
from pydantic import BaseModel, Field
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)


@tool
def getPackages(input:str  ) -> str:
   
    """
    Get a vacation package based on the location, budget, and duration of the trip
    """
    input = json.loads(input)
    location = input["location"]
    budget = input["budget"]
    duration = input["duration"]

    availablePackages = {
        "singapore": {
            "budget": "100000",
            "duration": "5",
            "package": "Singapore Tour Package"
        },
        "malaysia": {
            "budget": "8000",
            "duration": "4",
            "package": "Malaysia Tour Package"
        },
        "thailand": {
            "budget": "90000",
            "duration": "6",
            "package": "Thailand Tour Package"
        },
        "dubai": {
            "budget": "120000",
            "duration": "7",
            "package": "Dubai Tour Package"
        },
        "paris": {
            "budget": "150000",
            "duration": "8",
            "package": "Paris Tour Package"
        },
        "new york": {
            "budget": "200000",
            "duration": "10",
            "package": "New York Tour Package"
        }

    }

    if location not in availablePackages:
        return "I'm sorry, I don't have any information on that location. Please provide a different location."
    if int(budget) < int(availablePackages[location]["budget"]):
        return f"Based on your budget, I recommend increasing your budget to at least {availablePackages[location]['budget']} to afford the {availablePackages[location]['package']} package."
    if int(duration) < int(availablePackages[location]["duration"]):
        return f"Based on your duration, I recommend increasing your duration to at least {availablePackages[location]['duration']} days to enjoy the {availablePackages[location]['package']}"
    else:
        return f"Based on your location, budget, and duration, I recommend the {availablePackages[location]['package']} package."

class GetPackageInput(BaseModel):
    location: str = Field(description="The location you want to visit")
    budget: str = Field(description="The budget you have for the trip")
    duration: str = Field(description="The duration of the trip")


getPackageTools = StructuredTool.from_function(
    getPackages,
    name="GetPackage",
    description="Get a vacation package based on the location, budget, and duration of the trip",
    args_schema=GetPackageInput,
    return_direct=True
)

# class PackagesTool(BaseTool):
#     name = "Packages"
#     description = "Get a vacation package based on the location, budget, and duration of the trip"
#     args_schema:Type[GetPackageInput] = GetPackageInput
#     return_direct = True


#     def _run(
#         self, location:str,budget:str,duration:str, run_manager: Optional[CallbackManagerForToolRun] = None
#     ) -> str:
#         return getPackages(location,budget,duration)
    
#     async def _arun(
#         self, location:str,budget:str,duration:str, run_manager: Optional[CallbackManagerForToolRun] = None
#     ) -> str:
#         return getPackages(location,budget,duration)
    

    
