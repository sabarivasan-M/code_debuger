// DOM Elements
const fileInput = document.getElementById('file-input');
const analyzeBtn = document.getElementById('analyze-btn');
const loading = document.getElementById('loading');
const results = document.getElementById('results');
const securityScore = document.getElementById('security-score');
const performanceScore = document.getElementById('performance-score');
const maintainabilityScore = document.getElementById('maintainability-score');
const issuesList = document.getElementById('issues-list');
const suggestionsText = document.getElementById('suggestions-text');
const testsCode = document.getElementById('tests-code');
const originalCode = document.getElementById('original-code');
const fixedCodeDisplay = document.getElementById('fixed-code-display');
const fixedCodeComparison = document.getElementById('fixed-code-comparison');
const copyFixedBtn = document.getElementById('copy-fixed-btn');
const downloadFixedBtn = document.getElementById('download-fixed-btn');
const tabBtns = document.querySelectorAll('.tab-btn');
const tabPanes = document.querySelectorAll('.tab-pane');

// Event Listeners
analyzeBtn.addEventListener('click', analyzeCode);
copyFixedBtn.addEventListener('click', copyFixedCode);
downloadFixedBtn.addEventListener('click', downloadFixedCode);
tabBtns.forEach(btn => btn.addEventListener('click', switchTab));

// Functions
async function analyzeCode() {
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select a Python file to analyze.');
        return;
    }

    // Show loading
    loading.classList.remove('hidden');
    results.classList.add('hidden');

    try {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch('http://localhost:8000/analyze', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Analysis failed');
        }

        const data = await response.json();

        // Display results
        displayResults(data, await file.text());

    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        loading.classList.add('hidden');
    }
}

function displayResults(data, codeContent) {
    // Scores
    securityScore.textContent = data.security_score;
    performanceScore.textContent = data.performance_score;
    maintainabilityScore.textContent = data.maintainability_score;

    // Color scores
    colorScore('security-card', data.security_score);
    colorScore('performance-card', data.performance_score);
    colorScore('maintainability-card', data.maintainability_score);

    // Issues
    issuesList.innerHTML = '';
    data.issues.forEach(issue => {
        const li = document.createElement('li');
        li.textContent = `${issue.type}: ${issue.message} (line ${issue.line})`;
        issuesList.appendChild(li);
    });

    // Suggestions
    suggestionsText.textContent = data.suggestions;

    // Fixed Code
    fixedCodeDisplay.textContent = data.fixed_code;
    fixedCodeComparison.textContent = data.fixed_code;

    // Tests
    testsCode.textContent = data.generated_tests;

    // Original code
    originalCode.textContent = codeContent;

    // Show results
    results.classList.remove('hidden');
}

function colorScore(cardId, score) {
    const card = document.getElementById(cardId);
    const scoreEl = card.querySelector('.score');
    if (score >= 7) {
        scoreEl.style.color = '#ef4444'; // Danger
    } else if (score >= 4) {
        scoreEl.style.color = '#facc15'; // Warning
    } else {
        scoreEl.style.color = '#22c55e'; // Success
    }
}

async function copyFixedCode() {
    const fixedCode = fixedCodeDisplay.textContent;
    if (!fixedCode || fixedCode.trim() === '') {
        alert('No fixed code available to copy.');
        return;
    }

    try {
        await navigator.clipboard.writeText(fixedCode);
        // Visual feedback
        const btn = document.getElementById('copy-fixed-btn');
        const originalText = btn.textContent;
        btn.textContent = '✅ Copied!';
        btn.style.backgroundColor = '#22c55e';
        setTimeout(() => {
            btn.textContent = originalText;
            btn.style.backgroundColor = '';
        }, 2000);
    } catch (err) {
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = fixedCode;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);

        const btn = document.getElementById('copy-fixed-btn');
        const originalText = btn.textContent;
        btn.textContent = '✅ Copied!';
        btn.style.backgroundColor = '#22c55e';
        setTimeout(() => {
            btn.textContent = originalText;
            btn.style.backgroundColor = '';
        }, 2000);
    }
}

function downloadFixedCode() {
    const fixedCode = fixedCodeDisplay.textContent;
    if (!fixedCode || fixedCode.trim() === '') {
        alert('No fixed code available to download.');
        return;
    }

    const blob = new Blob([fixedCode], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = 'fixed_code.py';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

function switchTab(e) {
    const tab = e.target.dataset.tab;

    // Update buttons
    tabBtns.forEach(btn => btn.classList.remove('active'));
    e.target.classList.add('active');

    // Update panes
    tabPanes.forEach(pane => pane.classList.remove('active'));
    document.getElementById(tab + '-pane').classList.add('active');
}