from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="COE 558 Calculator API",
    description="A simple RESTful calculator API for addition, subtraction, multiplication, and division.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://www.coe558calculatorappalem.com",
        "http://localhost:8080",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str


def perform_calculation(num1: float, num2: float, operation: str) -> dict:
    normalized_operation = operation.lower().strip()

    if normalized_operation in ["add", "addition", "+"]:
        result = num1 + num2
        operation_name = "add"
    elif normalized_operation in ["subtract", "subtraction", "-"]:
        result = num1 - num2
        operation_name = "subtract"
    elif normalized_operation in ["multiply", "multiplication", "*"]:
        result = num1 * num2
        operation_name = "multiply"
    elif normalized_operation in ["divide", "division", "/"]:
        if num2 == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed.",
            )
        result = num1 / num2
        operation_name = "divide"
    else:
        raise HTTPException(
            status_code=400,
            detail="Unsupported operation. Supported operations are: add, subtract, multiply, divide.",
        )

    return {
        "num1": num1,
        "num2": num2,
        "operation": operation_name,
        "result": result,
    }


@app.get("/")
def root():
    return {
        "message": "COE 558 Calculator API is running.",
        "calculate_endpoint": "/calculate",
        "swagger_ui": "/docs",
        "openapi_schema": "/openapi.json",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/calculate")
def calculate_get(
        num1: float = Query(..., description="First number"),
        num2: float = Query(..., description="Second number"),
        operation: str = Query(..., description="add, subtract, multiply, or divide"),
):
    return perform_calculation(num1, num2, operation)


@app.post("/calculate")
def calculate_post(request: CalculationRequest):
    return perform_calculation(request.num1, request.num2, request.operation)