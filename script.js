document.getElementById('analyze-btn').addEventListener('click', function() {
    
    const review = document.getElementById('review-input').value
    
    if (review.trim() === '') {
        alert('Please write a review first')
        return
    }

    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({text: review})
    })
    .then(response => response.json())
    .then(data => {
        const badge = document.getElementById('label-badge')
        const confidence = document.getElementById('confidence-text')
        const result = document.getElementById('result')

        badge.textContent = data.label
        badge.className = data.label
        confidence.textContent = 'Confidence: ' + data.confidence + '%'
        
        result.classList.remove('hidden')
    })
})