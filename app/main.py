import uvicorn
from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel, Field, EmailStr

app = FastAPI()


@app.get("/", response_description="Wellcome to this fantastic API!")
async def root():
    return {"message": "Hello World, welcome to this fantastic API...!"}


@app.get("/api/fullname/v1/{firstName}/{lastName}", response_description="Capitalize input and return fullname")
async def get_full_name(firstName:str, lastName:str):
    fullName = f"{firstName.title()} {lastName.title()}"
    return {"fullname": fullName}


# using a class and input from request url #####################################################################################
class UserName():

    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName if firstName else ""
        self.lastName = lastName if lastName else ""

    def getFullName(self) -> str: 
        return f"{self.firstName.title()} {self.lastName.title()}"


@app.get("/api/fullname/v2/{firstName}/{lastName}", response_description="Capitalize input, using Python Object and return fullname")
async def get_full_name(firstName:str, lastName:str):
    
    print("Using the UserName Object...")
    
    obj = UserName(firstName, lastName)
    fullName = obj.getFullName()
    
    return {"fullname": fullName}


# Using pydantic and request body validation #####################################################################################

class UserNameSchema(BaseModel):    # this is used in input validation, when put async function definition ie reqBody: UserNameSchema = Body(...)
    firstName: str = Field()
    lastName: str = Field(...,min_length=2)  # required field
    email: EmailStr = Field()
    year: int = Field(gt=18, lt=109)
    class Config:                   # this will appear as an example in Swagger specs
        schema_extra = {
            "example": {
                "firstName": "georgios em",
                "lastName": "tzirtzilakis",
                "email": "tzirtzi@gmail.com",
                "year": 27
            }
        }


@app.post("/api/fullname/v2", response_description="Capitalize input, using Python Object from request body and return fullname")
async def get_full_name(reqBody: UserNameSchema = Body(...)):
    
    print("Using the request body...", reqBody)
    
    # You can use jsonable_encoder or alternatively, the following two lines
    # reqDict = {k: v for k, v in reqBody.dict().items() if v is not None}
    # userName = UserNameSchema(**reqDict)
        
    userName = jsonable_encoder(reqBody)    
    print("After decoding...", userName)
    fullName = f"{userName['firstName'].title()} {userName['lastName'].title()}"
    
    return {"fullname": fullName}


# this is for dev purposes, use command line for prod, 
# with workers and other params for optimal performance
if __name__ == "__main__" : 
    uvicorn.run ( "main:app", host="0.0.0.0", port=8000, reload = True)




