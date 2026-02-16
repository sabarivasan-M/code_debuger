from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import os
from analyzer import analyze_file
from scoring import calculate_security_score, calculate_performance_score, calculate_maintainability_score
from test_generator import generate_test_file

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    # Save uploaded file to temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        # Run analysis
        pylint_res, bandit_res, radon_res, issues, suggestions, fixed_code = analyze_file(tmp_path)

        # Calculate scores
        security_score = calculate_security_score(bandit_res)
        performance_score = calculate_performance_score(radon_res)
        maintainability_score = calculate_maintainability_score(pylint_res)

        # Generate tests
        generated_tests = generate_test_file(content.decode())

        return {
            "security_score": security_score,
            "performance_score": performance_score,
            "maintainability_score": maintainability_score,
            "issues": issues,
            "suggestions": suggestions,
            "fixed_code": fixed_code,
            "generated_tests": generated_tests
        }
    finally:
        # Clean up temp file
        os.unlink(tmp_path)